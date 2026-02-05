import uuid
from openg2p_pbms_models.models import G2PRegistry
from sqlalchemy import String, DateTime, Text, Boolean, Integer
from sqlalchemy.orm import Mapped, mapped_column

class G2PRegisterFamilies(G2PRegistry):
    __tablename__ = "g2p_register_families"


    family_name: Mapped[str] = mapped_column(String, nullable=True)
    type_of_housing: Mapped[str] = mapped_column(String, nullable=True)
    house_condition: Mapped[str] = mapped_column(String, nullable=True)
    sanitation_condition: Mapped[str] = mapped_column(String, nullable=True)
    water_access: Mapped[str] = mapped_column(String, nullable=True)
    electricity_access: Mapped[str] = mapped_column(String, nullable=True)
    ethnic_group: Mapped[str] = mapped_column(String, nullable=True)
    belong_to_protected_groups: Mapped[bool] = mapped_column(Boolean, nullable=True)
    under_other_vulnerable_status: Mapped[bool] = mapped_column(Boolean, nullable=True)

    # Addl fields
    no_of_children: Mapped[int] = mapped_column(Integer, nullable=True)
