from typing import Optional

from pydantic import BaseModel, Field

from app.schemas.mentor import MentorRead
from app.schemas.student import StudentRead


class FeedbackCreate(BaseModel):
    booking_id: int
    rating: int = Field(ge=1, le=5)
    comment: str


class FeedbackUpdate(BaseModel):
    rating: Optional[int] = Field(default=None, ge=1, le=5)
    comment: Optional[str] = None


class FeedbackResponse(BaseModel):
    id: int
    booking_id: int
    student_id: int
    mentor_id: int
    rating: int
    comment: str
    student: Optional[StudentRead] = None
    mentor: Optional[MentorRead] = None

    class Config:
        from_attributes = True


FeedbackRead = FeedbackResponse
