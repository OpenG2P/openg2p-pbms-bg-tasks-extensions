from typing import Optional

from .registry import G2PRegistryPayload


class G2PRegistryFamiliesPayload(G2PRegistryPayload):
    hof_individual_registry_id : Optional[int] = None
    hof_individual_unique_id: Optional[str] = None
    hof_individual_name: Optional[str] = None
