from typing import List, Dict

import numpy as np
from fastapi_cache.decorator import cache
from openg2p_bg_task_models.models import BeneficiaryListDetails
from openg2p_bg_task_models.schemas import (
    BeneficiarySearchResponsePayload,
    RegistrantDetails,
)
from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import Session

from ..cache import beneficiary_count_key_builder
from ..interface import RegistryInterface
from ..models import (
    BeneficiaryListSummaryFamilies as BeneficiaryListSummaryFamiliesModel,
    G2PRegistryFamilies,
)
from ..schema import (
    BeneficiaryListSummary,
    BeneficiaryListSummaryFamilies,
    BeneficiaryListSummaryFamiliesPayload,
    G2PRegistryFamiliesPayload,
)


class RegistryFamilies(RegistryInterface):
    """Fetches family data and computes summary statistics"""

    # ===================
    # Summary API Methods
    # ===================
    async def get_summary(
        self,
        beneficiary_list_id: str,
        bg_task_session: AsyncSession,
        formated: bool = False,
    ) -> BeneficiaryListSummaryFamiliesPayload:
        result = await bg_task_session.execute(
            select(BeneficiaryListSummaryFamiliesModel).where(
                BeneficiaryListSummaryFamiliesModel.beneficiary_list_id == beneficiary_list_id
            )
        )
        summary_families = result.scalars().first()
        if not summary_families:
            return None

        return BeneficiaryListSummaryFamiliesPayload(
            beneficiary_list_summary=BeneficiaryListSummary(
                id=summary_families.id,
                program_id=summary_families.program_id,
                program_mnemonic=summary_families.program_mnemonic,
                target_registry=summary_families.target_registry,
                beneficiary_list_id=summary_families.beneficiary_list_id,
                number_of_registrants=summary_families.number_of_registrants,
                date_created=summary_families.date_created,
                total_disbursement_quantity=summary_families.total_disbursement_quantity,
                average_entitlement_per_registrant=summary_families.average_entitlement_per_person,
            ),
            registry_summary=BeneficiaryListSummaryFamilies(
                entitlement_amount_q3=summary_families.entitlement_amount_q3,
                entitlement_amount_q2=summary_families.entitlement_amount_q2,
                entitlement_amount_q1=summary_families.entitlement_amount_q1,
            ),
        )

    def get_summary_sync(
        self, beneficiary_list_id: str, bg_task_session: Session
    ) -> BeneficiaryListSummaryFamiliesPayload:
        summary_families = (
            bg_task_session.query(BeneficiaryListSummaryFamiliesModel)
            .filter_by(beneficiary_list_id=beneficiary_list_id)
            .first()
        )
        if not summary_families:
            return None

        return BeneficiaryListSummaryFamiliesPayload(
            beneficiary_list_summary=BeneficiaryListSummary(
                id=summary_families.id,
                program_id=summary_families.program_id,
                program_mnemonic=summary_families.program_mnemonic,
                target_registry=summary_families.target_registry,
                beneficiary_list_id=summary_families.beneficiary_list_id,
                number_of_registrants=summary_families.number_of_registrants,
                date_created=summary_families.date_created,
                total_disbursement_quantity=summary_families.total_disbursement_quantity,
                average_entitlement_per_registrant=summary_families.average_entitlement_per_person,
            ),
            registry_summary=BeneficiaryListSummaryFamilies(
                entitlement_amount_q3=summary_families.entitlement_amount_q3,
                entitlement_amount_q2=summary_families.entitlement_amount_q2,
                entitlement_amount_q1=summary_families.entitlement_amount_q1,
            ),
        )

    # ==============================
    # Beneficiary Search API Methods
    # ==============================
    async def search_beneficiaries(
        self,
        bg_task_session: AsyncSession,
        sr_session: AsyncSession,
        beneficiary_list_id: str,
        target_registry: str,
        search_query,
        page=1,
        page_size=10,
        order_by="id asc",
    ) -> BeneficiarySearchResponsePayload:
        registrant_details_result = await bg_task_session.execute(
            select(BeneficiaryListDetails.registrant_details).where(
                BeneficiaryListDetails.beneficiary_list_id == beneficiary_list_id
            )
        )
        registrant_details = registrant_details_result.scalars().all()
        registrant_ids = [
            registrant["registrant_id"]
            for registrant_detail in registrant_details
            for registrant in registrant_detail
        ]

        families_search_query, families_search_params = self.construct_beneficiary_search_sql_query(
            registrant_ids, target_registry, search_query, order_by, page_size, page
        )
        families_search_results = (
            (await sr_session.execute(families_search_query, families_search_params))
            .mappings()
            .all()
        )

        total_beneficiary_count: int = await self._get_total_beneficiary_count(
            sr_session, beneficiary_list_id, registrant_ids, search_query
        )
        beneficiaries = [
            G2PRegistryFamiliesPayload(
                id=families.get("id"),
                unique_id=families.get("unique_id"),
                hof_individual_registry_id=families.get("hof_individual_registry_id"),
                hof_individual_unique_id=families.get("hof_individual_unique_id"),
                hof_individual_name=families.get("hof_individual_name"),
            )
            for families in families_search_results
        ] if families_search_results else []

        return BeneficiarySearchResponsePayload(
            total_beneficiary_count=total_beneficiary_count,
            page=page,
            page_size=page_size,
            beneficiaries=beneficiaries,
        )

    @cache(expire=120, key_builder=beneficiary_count_key_builder)
    async def _get_total_beneficiary_count(
        self,
        sr_session: AsyncSession,
        beneficiary_list_id: str,
        registrant_ids: List[str],
        search_query: str,
    ) -> int:
        beneficiary_count_query, beneficiary_count_params = self.construct_beneficiary_search_count_sql_query(
            registrant_ids, "families", search_query
        )
        total_beneficiary_count = (
            await sr_session.execute(beneficiary_count_query, beneficiary_count_params)
        ).scalar_one()
        return total_beneficiary_count

    # =================================
    # Eligibility Celery Families Methods
    # =================================
    def compute_eligibility_statistics(
        self,
        beneficiary_list_details: List[BeneficiaryListDetails],
        base_summary,
        sr_session: Session,
        bg_task_session: Session,
    ):
        families_summary = BeneficiaryListSummaryFamiliesModel(
            program_id=base_summary.program_id,
            program_mnemonic=base_summary.program_mnemonic,
            target_registry=base_summary.target_registry,
            beneficiary_list_id=base_summary.beneficiary_list_id,
            number_of_registrants=base_summary.number_of_registrants,
            date_created=base_summary.date_created,
        )

        bg_task_session.add(families_summary)

    def get_registrants_by_ids(
        self, registrant_ids: List[str], sr_session: Session
    ) -> List[G2PRegistryFamilies]:
        families = sr_session.query(G2PRegistryFamilies).filter(
            G2PRegistryFamilies.unique_id.in_(registrant_ids)
        )
        return list(families.yield_per(500))

    # =================================
    # Entitlement Celery Families Methods
    # =================================
    def get_is_registant_entitled(
        self, registrant_id: str, sql_query: str, sr_session: Session
    ) -> bool:
        sql_query_with_registrant_id = self.construct_get_is_registrant_entitled_sql_query(
            registrant_id, "families", sql_query
        )
        result = sr_session.execute(sql_query_with_registrant_id).fetchone()
        return result is not None

    def get_entitlement_multiplier(
        self, multiplier: str, registrant_id: str, sr_session: Session
    ) -> int:
        if not multiplier or multiplier == "none":
            return 1

        sql_query = self.construct_multiplier_sql_query(
            multiplier, target_registry="families"
        )
        params = {"registrant_id": registrant_id}
        result = sr_session.execute(sql_query, params).fetchone()
        return int(result[0]) if result and result[0] is not None else 1

    def compute_entitlement_statistics(
        self, beneficiary_list_id: str, bg_task_session: Session, sr_session: Session
    ):
        beneficiary_list_details = (
            bg_task_session.query(BeneficiaryListDetails)
            .filter_by(beneficiary_list_id=beneficiary_list_id)
            .all()
        )

        registrant_map_from_registry: Dict[str, G2PRegistryFamilies] = {}

        for beneficiary_list_detail in beneficiary_list_details:
            registrant_ids = [
                RegistrantDetails(**registrant_detail).registrant_id
                for registrant_detail in beneficiary_list_detail.registrant_details
            ]
            registrants_list: List[G2PRegistryFamilies] = self.get_registrants_by_ids(
                registrant_ids, sr_session
            )
            for registrant in registrants_list:
                registrant_map_from_registry[str(registrant.unique_id)] = registrant

        entitlements: Dict[int, list[float]] = {}

        for beneficiary_list_detail in beneficiary_list_details:
            for registrant_detail in beneficiary_list_detail.registrant_details:
                registrant_detail_obj = RegistrantDetails(**registrant_detail)
                registrant = registrant_map_from_registry.get(
                    str(registrant_detail_obj.registrant_id)
                )

                for benefit_code_id, value in registrant_detail_obj.entitlement.items():
                    entitlements.setdefault(benefit_code_id, []).append(value)

        entitlement_stats = self.compute_stats_dict(entitlements)

        bg_task_session.execute(
            update(BeneficiaryListSummaryFamiliesModel)
            .where(
                BeneficiaryListSummaryFamiliesModel.beneficiary_list_id == beneficiary_list_id
            )
            .values(
                total_disbursement_quantity=dict(entitlement_stats["total"]),
                average_entitlement_per_person=dict(entitlement_stats["average"]),
                entitlement_amount_q1=dict(entitlement_stats["q1"]),
                entitlement_amount_q2=dict(entitlement_stats["q2"]),
                entitlement_amount_q3=dict(entitlement_stats["q3"]),
            )
        )

    def compute_stats_dict(self, entitlements_dict: Dict[int, list[float]]) -> Dict[str, Dict[int, float]]:
        stats = {
            "average": {},
            "q1": {},
            "q2": {},
            "q3": {},
            "total": {},
        }
        for benefit_code_id, values in entitlements_dict.items():
            if not values:
                stats["average"][benefit_code_id] = 0.0
                stats["q1"][benefit_code_id] = 0.0
                stats["q2"][benefit_code_id] = 0.0
                stats["q3"][benefit_code_id] = 0.0
                stats["total"][benefit_code_id] = 0.0
            else:
                arr = np.array(values)
                stats["average"][benefit_code_id] = round(float(np.mean(arr)), 2)
                stats["q1"][benefit_code_id] = round(float(np.percentile(arr, 25, method="midpoint")), 2)
                stats["q2"][benefit_code_id] = round(float(np.percentile(arr, 50, method="midpoint")), 2)
                stats["q3"][benefit_code_id] = round(float(np.percentile(arr, 75, method="midpoint")), 2)
                stats["total"][benefit_code_id] = float(np.sum(arr))
        return stats
