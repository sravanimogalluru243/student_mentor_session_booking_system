from pydantic import BaseModel
from typing import Optional


class FeedbackBase(BaseModel):
    student_id: int
    mentor_id: int
    rating: int
    comments: Optional[str] = None


class FeedbackCreate(FeedbackBase):
    pass


class FeedbackRead(FeedbackBase):
    id: int

    class Config:
        from_attributes = True
