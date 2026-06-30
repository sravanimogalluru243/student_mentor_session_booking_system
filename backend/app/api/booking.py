from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session

from app.schemas.booking import BookingCreate, BookingRead
from app.database.connection import get_db
from app.services import booking_service

router = APIRouter(prefix="/bookings", tags=["bookings"])


@router.post("/", response_model=BookingRead)
def create_booking(booking_in: BookingCreate, db: Session = Depends(get_db)):
	# business rules (e.g., capacity) should be in service
	return booking_service.create_booking(db, booking_in)


@router.get("/", response_model=List[BookingRead])
def list_bookings(student_id: int = None, session_id: int = None, db: Session = Depends(get_db)):
	return booking_service.list_bookings(db, student_id=student_id, session_id=session_id)
