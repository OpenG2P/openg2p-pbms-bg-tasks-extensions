from sqlalchemy import String, Integer
from sqlalchemy.orm import mapped_column

from openg2p_pbms_models.models import G2PRegistry


class G2PRegistryProfessionalTaxPayers(G2PRegistry):
    __tablename__ = "g2p_registry_professional_tax_payers"

    ration_card_application_id = mapped_column(String, nullable=True)
    individual_registry_id = mapped_column(Integer, nullable=True)
    individual_unique_id = mapped_column(String, nullable=True)
    applicant_aadhaar = mapped_column(String, nullable=True)
    family_unique_id = mapped_column(String, nullable=True)
    family_registry_id = mapped_column(Integer, nullable=True)
    type_of_business = mapped_column(String, nullable=True)
