from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.booking import BookingRead
from app.schemas.student import StudentRead, StudentUpdate
from app.services import student_service

router = APIRouter(prefix="/students", tags=["students"])


@router.get("/profile", response_model=StudentRead)
def get_profile(student_id: int, db: Session = Depends(get_db)):
    return student_service.get_profile(db, student_id)


@router.put("/profile", response_model=StudentRead)
def update_profile(
    student_id: int,
    student_in: StudentUpdate,
    db: Session = Depends(get_db)
):
    return student_service.update_profile(db, student_id, student_in)


@router.get("/bookings", response_model=List[BookingRead])
def get_student_bookings(student_id: int, db: Session = Depends(get_db)):
    return student_service.get_student_bookings(db, student_id)


@router.get("/history", response_model=List[BookingRead])
def get_booking_history(student_id: int, db: Session = Depends(get_db)):
    return student_service.get_booking_history(db, student_id)