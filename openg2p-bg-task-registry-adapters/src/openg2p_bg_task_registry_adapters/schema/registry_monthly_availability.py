from typing import Optional

from .registry import G2PRegistryPayload


class G2PRegistryMonthlyAvailabilityPayload(G2PRegistryPayload):
    unique_id: Optional[int] = None
    name: Optional[str] = None
    attendance_month_str: Optional[str] = None
    attendance_month: Optional[str] = None
    source_type: Optional[str] = None
