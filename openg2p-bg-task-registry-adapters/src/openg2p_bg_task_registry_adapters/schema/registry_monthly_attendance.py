from typing import Optional
from datetime import date

from .registry import G2PRegistryPayload


class G2PRegistryMonthlyAttendancePayload(G2PRegistryPayload):
    unique_id: Optional[int] = None
    nrc_number: Optional[str] = None
    attendance_month: Optional[date] = None
    number_of_days: Optional[str] = None
