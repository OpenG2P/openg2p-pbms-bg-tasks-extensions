from sqlalchemy import String, Integer, Date
from sqlalchemy.orm import mapped_column

from openg2p_pbms_models.models import G2PRegistry


class G2PRegistryVehicleOwnership(G2PRegistry):
    __tablename__ = "g2p_registry_vehicle_ownership"

    vehicle_registration_id = mapped_column(String, nullable=True, doc="Unique identifier for the vehicle registration")

    # Standard registry fields (present in all models except ration card)
    individual_registry_id = mapped_column(Integer, nullable=True, doc="Reference to individual registry record")
    individual_unique_id = mapped_column(String, nullable=True, doc="MOSIP generated unique ID for individual")
    owner_aadhaar = mapped_column(String, nullable=True, doc="Aadhaar number of the vehicle owner")
    family_unique_id = mapped_column(String, nullable=True, doc="MOSIP generated unique ID for family")
    family_registry_id = mapped_column(Integer, nullable=True, doc="Reference to family registry record")

    # Vehicle details
    class_of_vehicle = mapped_column(String, nullable=True, doc="Classification type of the vehicle")
    number_of_wheels = mapped_column(Integer, nullable=True, doc="Number of wheels of the vehicle")
    registration_from_date = mapped_column(Date, nullable=True, doc="Vehicle registration start date")
    registration_to_date = mapped_column(Date, nullable=True, doc="Vehicle registration end date")
    engine_no = mapped_column(String, nullable=True, doc="Engine number of the vehicle")
    chassis_no = mapped_column(String, nullable=True, doc="Chassis number of the vehicle")
    manufacturer = mapped_column(String, nullable=True, doc="Vehicle manufacturer name")
