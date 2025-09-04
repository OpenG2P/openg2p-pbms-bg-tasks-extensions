from openg2p_bg_task_models.errors import BGTaskErrorCodes, BGTaskException

from ..computations import (
    RegistryRationCardApplicants,
    RegistryIndividuals,
    RegistryFamilies,
    RegistryElecMonthlyAvg,
    RegistryGovtEmployees,
    RegistryLandHoldings,
    RegistryLrsBrsApplication,
    RegistryProfessionalTaxPayers,
    RegistryResidentialHouses,
    RegistryVehicleOwnership,
)
from ..interface import RegistryInterface
from ..models import G2PRegistryType


class RegistryFactory:
    """Get the appropriate summary computation class based on the registrant type"""

    @staticmethod
    def get_registry_class(
        target_registry,
    ) -> RegistryInterface:

        if target_registry == G2PRegistryType.RATION_CARD_APPLICANTS.value:
            return RegistryRationCardApplicants()
        elif target_registry == G2PRegistryType.INDIVIDUALS.value:
            return RegistryIndividuals()
        elif target_registry == G2PRegistryType.FAMILIES.value:
            return RegistryFamilies()
        elif target_registry == G2PRegistryType.ELEC_MONTHLY_AVG.value:
            return RegistryElecMonthlyAvg()
        elif target_registry == G2PRegistryType.GOVT_EMPLOYEES.value:
            return RegistryGovtEmployees()
        elif target_registry == G2PRegistryType.LAND_HOLDINGS.value:
            return RegistryLandHoldings()
        elif target_registry == G2PRegistryType.LRS_BRS_APPLICATION.value:
            return RegistryLrsBrsApplication()
        elif target_registry == G2PRegistryType.PROFESSIONAL_TAX_PAYERS.value:
            return RegistryProfessionalTaxPayers()
        elif target_registry == G2PRegistryType.RESIDENTIAL_HOUSES.value:
            return RegistryResidentialHouses()
        elif target_registry == G2PRegistryType.VEHICLE_OWNERSHIP.value:
            return RegistryVehicleOwnership()

        else:
            raise BGTaskException(code=BGTaskErrorCodes.INVALID_REQUEST)
