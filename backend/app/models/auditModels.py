from pydantic import BaseModel
from typing import Optional

class AuditRequest(BaseModel):
    url: Optional[str] = None
    html: Optional[str] = None
