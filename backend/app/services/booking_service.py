from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.booking import Booking
from app.models.mentor import Mentor
from app.models.student import Student


VALID_STATUSES = {"Pending", "Accepted", "Rejected", "Completed", "Cancelled"}


def create_booking(db: Session, student_id: int, booking_in) -> Booking:
    mentor = db.query(Mentor).filter(Mentor.id == booking_in.mentor_id).first()
    if not mentor:
        raise HTTPException(status_code=404, detail="Mentor not found")

    existing = db.query(Booking).filter(
        Booking.mentor_id == booking_in.mentor_id,
        Booking.booking_date == booking_in.booking_date,
        Booking.booking_time == booking_in.booking_time,
        Booking.status.in_(["Pending", "Accepted"]),
    ).first()
    if existing:
        raise HTTPException(status_code=409, detail="Mentor already booked for this slot")

    booking = Booking(
        student_id=student_id,
        mentor_id=booking_in.mentor_id,
        booking_date=booking_in.booking_date,
        booking_time=booking_in.booking_time,
        status="Pending",
    )
    db.add(booking)
    db.commit()
    db.refresh(booking)
    return booking


def get_student_bookings(db: Session, student_id: int) -> list[Booking]:
    return db.query(Booking).filter(Booking.student_id == student_id).all()


def get_mentor_bookings(db: Session, mentor_id: int) -> list[Booking]:
    return db.query(Booking).filter(Booking.mentor_id == mentor_id).all()


def get_all_bookings(db: Session) -> list[Booking]:
    return db.query(Booking).all()


def get_booking(db: Session, booking_id: int) -> Booking:
    booking = db.query(Booking).filter(Booking.id == booking_id).first()
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking


def get_student_booking(db: Session, student_id: int, booking_id: int) -> Booking:
    booking = get_booking(db, booking_id)
    if booking.student_id != student_id:
        raise HTTPException(status_code=403, detail="Booking does not belong to this student")
    return booking


def update_booking_status(db: Session, booking_id: int, status: str) -> Booking:
    if status not in VALID_STATUSES:
        raise HTTPException(status_code=400, detail="Invalid booking status")

    booking = get_booking(db, booking_id)
    booking.status = status
    db.commit()
    db.refresh(booking)
    return booking


def mentor_update_booking_status(
    db: Session,
    mentor_id: int,
    booking_id: int,
    status: str,
) -> Booking:
    booking = get_booking(db, booking_id)
    if booking.mentor_id != mentor_id:
        raise HTTPException(status_code=403, detail="Booking does not belong to this mentor")
    return update_booking_status(db, booking_id, status)


def cancel_booking(db: Session, student_id: int, booking_id: int) -> Booking:
    booking = get_student_booking(db, student_id, booking_id)
    if booking.status == "Completed":
        raise HTTPException(status_code=400, detail="Completed bookings cannot be cancelled")
    booking.status = "Cancelled"
    db.commit()
    db.refresh(booking)
    return booking


def delete_booking(db: Session, booking_id: int) -> dict:
    booking = get_booking(db, booking_id)
    db.delete(booking)
    db.commit()
    return {"message": "Booking deleted successfully"}
