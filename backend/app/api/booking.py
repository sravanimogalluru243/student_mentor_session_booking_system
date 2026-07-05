from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.dependencies import get_current_admin, get_current_mentor, get_current_student
from app.models.admin import Admin
from app.models.mentor import Mentor
from app.models.student import Student
from app.schemas.booking import BookingCreate, BookingResponse
from app.services import booking_service


router = APIRouter(prefix="/bookings", tags=["Bookings"])


@router.post("/", response_model=BookingResponse)
def create_booking(
    booking: BookingCreate,
    db: Session = Depends(get_db),
    current_student: Student = Depends(get_current_student),
):
    return booking_service.create_booking(db, current_student.id, booking)


@router.get("/my", response_model=list[BookingResponse])
def get_my_bookings(
    db: Session = Depends(get_db),
    current_student: Student = Depends(get_current_student),
):
    return booking_service.get_student_bookings(db, current_student.id)


@router.get("/mentor/my", response_model=list[BookingResponse])
def get_mentor_bookings(
    db: Session = Depends(get_db),
    current_mentor: Mentor = Depends(get_current_mentor),
):
    return booking_service.get_mentor_bookings(db, current_mentor.id)


@router.get("/", response_model=list[BookingResponse])
def get_all_bookings(
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin),
):
    return booking_service.get_all_bookings(db)


@router.get("/{booking_id}", response_model=BookingResponse)
def get_booking(
    booking_id: int,
    db: Session = Depends(get_db),
    current_student: Student = Depends(get_current_student),
):
    return booking_service.get_student_booking(db, current_student.id, booking_id)


@router.patch("/{booking_id}/cancel", response_model=BookingResponse)
def cancel_booking(
    booking_id: int,
    db: Session = Depends(get_db),
    current_student: Student = Depends(get_current_student),
):
    return booking_service.cancel_booking(db, current_student.id, booking_id)


@router.delete("/{booking_id}")
def delete_booking(
    booking_id: int,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin),
):
    return booking_service.delete_booking(db, booking_id)
