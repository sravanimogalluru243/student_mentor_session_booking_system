from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class SessionBase(BaseModel):
    mentor_id: int
    title: str
    description: Optional[str] = None
    start_time: datetime
    end_time: datetime
    capacity: int = 1


class SessionCreate(SessionBase):
    pass


class SessionUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    capacity: Optional[int] = None


class SessionRead(SessionBase):
    id: int

    class Config:
        from_attributes = True
