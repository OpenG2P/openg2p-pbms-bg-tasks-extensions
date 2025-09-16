from openg2p_pbms_models.models import G2PRegistry
from sqlalchemy import String
from sqlalchemy.orm import mapped_column

class G2PRegistryMonthlyAvailability(G2PRegistry):
    __tablename__ = "g2p_monthly_availability_registry"

    name = mapped_column(String, nullable=True)
    attendance_month_str = mapped_column(String, nullable=True)
    attendance_month = mapped_column(String, nullable=True)
    source_type = mapped_column(String, nullable=True)
