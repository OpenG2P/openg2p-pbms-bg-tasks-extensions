from typing import List

from fastapi_cache.decorator import cache
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from ..cache import beneficiary_count_key_builder
from ..interface import RegistryInterface


class RegistryLandHoldings(RegistryInterface):
    """Fetches land_holdings data and computes summary statistics"""

    async def get_summary(
        self,
        beneficiary_list_id: str,
        bg_task_session: AsyncSession,
        formated: bool = False,
    ):
        return await super().get_summary(
            beneficiary_list_id, bg_task_session, formated
        )

    def get_summary_sync(
        self, beneficiary_list_id: str, bg_task_session: Session
    ):
        return super().get_summary_sync(beneficiary_list_id, bg_task_session)

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
    ):
        return await super().search_beneficiaries(
            bg_task_session,
            sr_session,
            beneficiary_list_id,
            target_registry,
            search_query,
            page,
            page_size,
            order_by,
        )

    @cache(expire=120, key_builder=beneficiary_count_key_builder)
    async def _get_total_beneficiary_count(
        self,
        sr_session: AsyncSession,
        beneficiary_list_id: str,
        registrant_ids: List[str],
        search_query: str,
    ) -> int:
        return await super()._get_total_beneficiary_count(
            sr_session,
            beneficiary_list_id,
            registrant_ids,
            search_query,
        )

    def compute_eligibility_statistics(
        self,
        beneficiary_list_details,
        base_summary,
        sr_session,
        bg_task_session,
    ):
        return super().compute_eligibility_statistics(
            beneficiary_list_details, base_summary, sr_session, bg_task_session
        )

    def get_registrants_by_ids(
        self, registrant_ids, sr_session
    ):
        return super().get_registrants_by_ids(registrant_ids, sr_session)

    def compute_entitlement_statistics(
        self, beneficiary_list_id: str, bg_task_session: Session, sr_session: Session
    ):
        return super().compute_entitlement_statistics(
            beneficiary_list_id, bg_task_session, sr_session
        )

    def compute_stats_dict(self, entitlements_dict: dict[int, list[float]]) -> dict:
        return super().compute_stats_dict(entitlements_dict)

    # =================================
    # Entitlement Celery Worker Methods
    # =================================
    def get_is_registant_entitled(
        self, registrant_id: str, sql_query: str, sr_session: Session
    ) -> bool:
        sql_query_with_registrant_id = self.construct_get_is_registrant_entitled_sql_query(
            registrant_id, "land_holdings", sql_query
        )
        result = sr_session.execute(sql_query_with_registrant_id).fetchone()
        return result is not None

    def get_entitlement_multiplier(
        self, multiplier: str, registrant_id: str, sr_session: Session
    ) -> int:
        if not multiplier or multiplier == "none":
            return 1

        sql_query = self.construct_multiplier_sql_query(
            multiplier, target_registry="land_holdings"
        )
        params = {"registrant_id": registrant_id}
        result = sr_session.execute(sql_query, params).fetchone()
        return int(result[0]) if result and result[0] is not None else 1
