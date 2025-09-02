from sqlalchemy import String, Integer
from sqlalchemy.orm import mapped_column

from openg2p_pbms_models.models import G2PRegistry


class G2PRegistryFamilies(G2PRegistry):
    __tablename__ = "g2p_registry_families"

    family_unique_id = mapped_column(String, nullable=True, doc="MOSIP generated unique ID for family")
    hof_individual_registry_id = mapped_column(Integer, nullable=True, doc="Registry ID of the Head of Family (HOF) individual")
    hof_individual_unique_id = mapped_column(String, nullable=True, doc="MOSIP generated unique ID for the Head of Family (HOF)")
    hof_individual_name = mapped_column(String, nullable=True, doc="Name of the Head of Family (HOF)")
