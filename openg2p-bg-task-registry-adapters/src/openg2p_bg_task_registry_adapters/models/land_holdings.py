from sqlalchemy import String, Integer, Float
from sqlalchemy.orm import mapped_column

from openg2p_pbms_models.models import G2PRegistry


class G2PLandHoldings(G2PRegistry):
    __tablename__ = "g2p_registry_land_holdings"

    individual_registry_id = mapped_column(Integer, nullable=True)
    individual_unique_id = mapped_column(String, nullable=True)
    aadhaar_id = mapped_column(String, nullable=True)
    family_unique_id = mapped_column(String, nullable=True)
    family_registry_id = mapped_column(Integer, nullable=True)
    property_id_tax_records = mapped_column(String, nullable=True)
    land_area_in_acres = mapped_column(Float, nullable=True)
