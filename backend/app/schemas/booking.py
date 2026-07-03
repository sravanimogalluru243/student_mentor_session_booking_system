from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class BookingBase(BaseModel):
    student_id: int
    session_id: int
    booked_at: Optional[datetime] = None


class BookingCreate(BookingBase):
    pass


class BookingRead(BookingBase):
    id: int

    class Config:
        from_attributes = True

