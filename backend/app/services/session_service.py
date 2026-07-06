from sqlalchemy.orm import Session

from app.services import booking_service


def get_student_sessions(db: Session, student_id: int):
    return booking_service.get_student_bookings(db, student_id)


def get_mentor_sessions(db: Session, mentor_id: int):
    return booking_service.get_mentor_bookings(db, mentor_id)


def complete_session(db: Session, mentor_id: int, booking_id: int):
    return booking_service.mentor_update_booking_status(
        db,
        mentor_id,
        booking_id,
        "Completed",
    )
