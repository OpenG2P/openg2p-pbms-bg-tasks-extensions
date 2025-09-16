from openg2p_pbms_models.models import G2PRegistry
from sqlalchemy import String, Date
from sqlalchemy.orm import mapped_column

class G2PRegistryMonthlyAttendance(G2PRegistry):
    __tablename__ = "g2p_monthly_attendance_registry"

    nrc_number = mapped_column(String, nullable=True)
    attendance_month = mapped_column(Date, nullable=True)
    number_of_days = mapped_column(String, nullable=True)
