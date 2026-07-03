from typing import List, Optional

from app.models.booking import Booking
from app.schemas.booking import BookingCreate


def create_booking(db, booking_in: BookingCreate) -> Booking:
    booking = Booking(**booking_in.dict())
    db.add(booking)
    db.commit()
    db.refresh(booking)
    return booking


def get_booking(db, booking_id: int) -> Optional[Booking]:
    return db.query(Booking).filter(Booking.id == booking_id).first()


def list_bookings(db, student_id: int = None, session_id: int = None) -> List[Booking]:
    query = db.query(Booking)
    if student_id is not None:
        query = query.filter(Booking.student_id == student_id)
    if session_id is not None:
        query = query.filter(Booking.session_id == session_id)
    return query.all()
