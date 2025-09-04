from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import mapped_column

from openg2p_pbms_models.models import G2PRegistry


class G2PRegistryIndividuals(G2PRegistry):
    __tablename__ = "g2p_registry_individuals"

    individual_unique_id = mapped_column(String, nullable=True, doc="MOSIP generated unique ID for individual")
    aadhaar_id = mapped_column(String, nullable=True, doc="Aadhaar number of the individual")
    family_unique_id = mapped_column(String, nullable=True, doc="MOSIP generated unique ID for family")
    family_registry_id = mapped_column(Integer, nullable=True, doc="Reference to family registry record")
    ration_card_id = mapped_column(String, nullable=True, doc="Ration card identifier")
    praja_palana_id = mapped_column(String, nullable=True, doc="Praja Palana identifier")
    icdb_id = mapped_column(String, nullable=True, doc="ICDB identifier")
    name = mapped_column(String, nullable=True, doc="Full name of the individual")
    family_name = mapped_column(String, nullable=True, doc="Family name of the individual")
    given_name = mapped_column(String, nullable=True, doc="Given name of the individual")
    gender = mapped_column(String, nullable=True, doc="Gender of the individual")
    village = mapped_column(String, nullable=True, doc="Village of residence")
    mandal_string = mapped_column(String, nullable=True, doc="Mandal of residence")
    district_string = mapped_column(String, nullable=True, doc="District of residence")
    address = mapped_column(Text, nullable=True, doc="Full address of the individual")
