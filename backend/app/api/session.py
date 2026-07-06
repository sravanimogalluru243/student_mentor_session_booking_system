from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.dependencies import get_current_mentor, get_current_student
from app.models.mentor import Mentor
from app.models.student import Student
from app.schemas.booking import BookingResponse
from app.services import booking_service


router = APIRouter(prefix="/sessions", tags=["Sessions"])


@router.get("/student", response_model=list[BookingResponse])
def get_student_sessions(
    db: Session = Depends(get_db),
    current_student: Student = Depends(get_current_student),
):
    return booking_service.get_student_bookings(db, current_student.id)


@router.get("/mentor", response_model=list[BookingResponse])
def get_mentor_sessions(
    db: Session = Depends(get_db),
    current_mentor: Mentor = Depends(get_current_mentor),
):
    return booking_service.get_mentor_bookings(db, current_mentor.id)


@router.patch("/{booking_id}/complete", response_model=BookingResponse)
def complete_session(
    booking_id: int,
    db: Session = Depends(get_db),
    current_mentor: Mentor = Depends(get_current_mentor),
):
    return booking_service.mentor_update_booking_status(
        db,
        current_mentor.id,
        booking_id,
        "Completed",
    )
