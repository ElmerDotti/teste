from pydantic import BaseModel
from datetime import datetime

class Message(BaseModel):
    id: int
    session_id: int
    content: str
    remote: bool
    created_at: datetime

class Analysis(BaseModel):
    session_id: int
    satisfaction: int
    summary: str
    improvement: str
    created_at: datetime
