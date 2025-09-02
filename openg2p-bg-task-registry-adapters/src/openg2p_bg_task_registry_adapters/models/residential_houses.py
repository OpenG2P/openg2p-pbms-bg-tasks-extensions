from sqlalchemy import String, Integer, Float
from sqlalchemy.orm import mapped_column

from openg2p_pbms_models.models import G2PRegistry


class G2PRegistryResidentialHouses(G2PRegistry):
    __tablename__ = "g2p_registry_residential_houses"

    individual_registry_id = mapped_column(Integer, nullable=True)
    individual_unique_id = mapped_column(String, nullable=True)
    aadhaar_id = mapped_column(String, nullable=True)
    family_unique_id = mapped_column(String, nullable=True)
    family_registry_id = mapped_column(Integer, nullable=True)
    property_id_tax_records = mapped_column(String, nullable=True)
    built_up_area_in_sq_feet = mapped_column(Float, nullable=True)
