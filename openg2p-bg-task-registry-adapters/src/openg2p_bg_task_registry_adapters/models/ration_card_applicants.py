from sqlalchemy import String, Integer, Date, DateTime
from sqlalchemy.orm import mapped_column

from openg2p_pbms_models.models import G2PRegistry


class G2PRegistryRationCardApplicants(G2PRegistry):
    __tablename__ = "g2p_registry_ration_card_applicants"

    ration_card_application_id = mapped_column(String, nullable=True)
    individual_registry_id = mapped_column(Integer, nullable=True)
    individual_unique_id = mapped_column(String, nullable=True)
    applicant_aadhaar = mapped_column(String, nullable=True)
    family_unique_id = mapped_column(String, nullable=True)
    family_registry_id = mapped_column(Integer, nullable=True)
    application_date = mapped_column(Date, nullable=True)
    verified_by = mapped_column(String, nullable=True)
    verification_time_stamp = mapped_column(DateTime, nullable=True)
    application_channel = mapped_column(String, nullable=True)
