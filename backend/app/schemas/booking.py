from datetime import date, time
from typing import Optional

from pydantic import BaseModel

from app.schemas.mentor import MentorRead
from app.schemas.student import StudentRead


class BookingCreate(BaseModel):
    mentor_id: int
    booking_date: date
    booking_time: time


class BookingStatusUpdate(BaseModel):
    status: str


class BookingResponse(BaseModel):
    id: int
    student_id: int
    mentor_id: int
    booking_date: date
    booking_time: time
    status: str
    attendance: Optional[str] = None

    student: Optional[StudentRead] = None
    mentor: Optional[MentorRead] = None
    class Config:
        from_attributes = True


BookingRead = BookingResponse
