from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session

from app.schemas.feedback import FeedbackCreate, FeedbackRead
from app.database.connection import get_db
from app.models.feedback import Feedback

router = APIRouter(prefix="/feedback", tags=["feedback"])


@router.post("/", response_model=FeedbackRead)
def create_feedback(feedback_in: FeedbackCreate, db: Session = Depends(get_db)):
    fb = Feedback(**feedback_in.dict())
    db.add(fb)
    db.commit()
    db.refresh(fb)
    return fb


@router.get("/", response_model=List[FeedbackRead])
def list_feedbacks(db: Session = Depends(get_db)):
    return db.query(Feedback).all()