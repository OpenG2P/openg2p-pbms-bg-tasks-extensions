from openg2p_bg_task_models.errors import BGTaskErrorCodes, BGTaskException

from ..computations import (
    RegistryWorker,
    RegistryMonthlyAttendance,
    RegistryMonthlyAvailability
)
from ..interface import RegistryInterface
from ..models import G2PRegistryType


class RegistryFactory:
    """Get the appropriate summary computation class based on the registrant type"""

    @staticmethod
    def get_registry_class(
        target_registry,
    ) -> RegistryInterface:
        
        if target_registry == G2PRegistryType.WORKER.value:
            return RegistryWorker()
        
        elif target_registry == G2PRegistryType.MONTHLY_ATTENDANCE.value:
            return RegistryMonthlyAttendance()
        
        elif target_registry == G2PRegistryType.MONTHLY_AVAILABILITY.value:
            return RegistryMonthlyAvailability()

        else:
            raise BGTaskException(code=BGTaskErrorCodes.INVALID_REQUEST)
