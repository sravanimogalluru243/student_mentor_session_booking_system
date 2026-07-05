from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.dependencies import get_current_admin, get_current_student
from app.models.admin import Admin
from app.models.student import Student
from app.schemas.feedback import FeedbackCreate, FeedbackResponse
from app.services import feedback_service


router = APIRouter(prefix="/feedback", tags=["Feedback"])


@router.post("/", response_model=FeedbackResponse)
def create_feedback(
    feedback: FeedbackCreate,
    db: Session = Depends(get_db),
    current_student: Student = Depends(get_current_student),
):
    return feedback_service.create_feedback(db, current_student.id, feedback)


@router.get("/my", response_model=list[FeedbackResponse])
def get_my_feedback(
    db: Session = Depends(get_db),
    current_student: Student = Depends(get_current_student),
):
    return feedback_service.get_student_feedback(db, current_student.id)


@router.get("/", response_model=list[FeedbackResponse])
def get_all_feedback(
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin),
):
    return feedback_service.get_all_feedback(db)
