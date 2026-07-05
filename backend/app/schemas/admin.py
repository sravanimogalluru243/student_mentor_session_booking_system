from typing import Optional

from pydantic import BaseModel, EmailStr

from app.schemas.booking import BookingResponse as BookingResponse
from app.schemas.feedback import FeedbackResponse as FeedbackResponse
from app.schemas.mentor import MentorCreate, MentorRead as MentorResponse, MentorUpdate
from app.schemas.student import StudentRead as StudentResponse


class AdminCreate(BaseModel):
    full_name: str
    email: EmailStr
    password: str


class AdminUpdate(BaseModel):
    full_name: Optional[str] = None
    password: Optional[str] = None


class AdminRead(BaseModel):
    id: int
    full_name: str
    email: EmailStr

    class Config:
        from_attributes = True


class DashboardResponse(BaseModel):
    total_students: int
    total_mentors: int
    total_bookings: int
    total_feedbacks: int

