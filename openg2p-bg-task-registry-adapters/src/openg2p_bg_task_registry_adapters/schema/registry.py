from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class G2PRegistryPayload(BaseModel):
    id: int
    link_registry_id: str
