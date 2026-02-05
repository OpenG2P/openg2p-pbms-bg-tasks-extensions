from typing import Optional

from .registry import G2PRegistryPayload


class G2PRegisterFamiliesPayload(G2PRegistryPayload):

    family_name: str
    type_of_housing: Optional[str] = None
    house_condition: Optional[str] = None
    sanitation_condition: Optional[str] = None
    water_access: Optional[str] = None
    electricity_access: Optional[str] = None
    ethnic_group: Optional[str] = None
    belong_to_protected_groups: Optional[bool] = None
    under_other_vulnerable_status: Optional[bool] = None

    # Addl fields
    no_of_children: Optional[int] = None
