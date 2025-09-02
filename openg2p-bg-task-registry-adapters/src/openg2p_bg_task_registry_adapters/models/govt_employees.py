from sqlalchemy import String, Integer, Date
from sqlalchemy.orm import mapped_column

from openg2p_pbms_models.models import G2PRegistry


class G2PRegistryGovtEmployees(G2PRegistry):
    __tablename__ = "g2p_registry_govt_employees"

    ration_card_application_id = mapped_column(String, nullable=True)
    individual_registry_id = mapped_column(Integer, nullable=True)
    individual_unique_id = mapped_column(String, nullable=True)
    applicant_aadhaar = mapped_column(String, nullable=True)
    family_unique_id = mapped_column(String, nullable=True)
    family_registry_id = mapped_column(Integer, nullable=True)
    government_department = mapped_column(String, nullable=True)
    employee_since_date = mapped_column(Date, nullable=True)
    type_of_department = mapped_column(String, nullable=True)
