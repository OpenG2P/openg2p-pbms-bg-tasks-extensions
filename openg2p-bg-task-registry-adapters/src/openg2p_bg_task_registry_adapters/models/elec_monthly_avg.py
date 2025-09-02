from sqlalchemy import String, Integer, Float, Date
from sqlalchemy.orm import mapped_column

from openg2p_pbms_models.models import G2PRegistry


class G2PRegistryElecMonthlyAvg(G2PRegistry):
    __tablename__ = "g2p_registry_elec_monthly_avg"

    ration_card_application_id = mapped_column(String, nullable=True)
    individual_registry_id = mapped_column(Integer, nullable=True)
    individual_unique_id = mapped_column(String, nullable=True)
    applicant_aadhaar = mapped_column(String, nullable=True)
    family_unique_id = mapped_column(String, nullable=True)
    family_registry_id = mapped_column(Integer, nullable=True)
    date_of_computation = mapped_column(Date, nullable=True)
    six_month_avg_units = mapped_column(Float, nullable=True)
    six_month_avg_amount = mapped_column(Float, nullable=True)
