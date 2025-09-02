from typing import Optional

from .registry import G2PRegistryPayload

class G2PRegistryIndividualsPayload(G2PRegistryPayload):
    individual_unique_id: Optional[str] = None
    aadhaar_id: Optional[str] = None
    family_unique_id: Optional[str] = None
    family_registry_id: Optional[int] = None
    ration_card_id: Optional[str] = None
    praja_palana_id: Optional[str] = None
    icdb_id: Optional[str] = None
    name: Optional[str] = None
    family_name: Optional[str] = None
    given_name: Optional[str] = None
    gender: Optional[str] = None
    village: Optional[str] = None
    mandal_string: Optional[str] = None
    district_string: Optional[str] = None
    address: Optional[str] = None
