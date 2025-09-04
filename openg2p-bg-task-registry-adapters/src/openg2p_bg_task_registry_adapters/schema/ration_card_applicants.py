from typing import Optional
from datetime import date, datetime

from .registry import G2PRegistryPayload


class G2PRegistryRationCardApplicantsPayload(G2PRegistryPayload):
    ration_card_application_id: Optional[str] = None
    individual_registry_id: Optional[int] = None
    individual_unique_id: Optional[str] = None
    aadhaar_id: Optional[str] = None
    family_unique_id: Optional[str] = None
    family_registry_id: Optional[int] = None
    application_date: Optional[date] = None
    verified_by: Optional[str] = None
    verification_time_stamp: Optional[datetime] = None
    application_channel: Optional[str] = None
