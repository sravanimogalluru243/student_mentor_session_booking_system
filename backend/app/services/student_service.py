from typing import List, Optional

from app.models.booking import Booking
from app.models.student import Student
from app.schemas.student import StudentUpdate


def get_profile(db, student_id: int) -> Optional[Student]:
    return db.query(Student).filter(Student.id == student_id).first()


def update_profile(db, student_id: int, student_in: StudentUpdate) -> Optional[Student]:
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        return None
    if student_in.name is not None:
        student.name = student_in.name
    if student_in.email is not None:
        student.email = student_in.email
    db.commit()
    db.refresh(student)
    return student


def get_student_bookings(db, student_id: int) -> List[Booking]:
    return db.query(Booking).filter(Booking.student_id == student_id).all()


def get_booking_history(db, student_id: int) -> List[Booking]:
    return db.query(Booking).filter(Booking.student_id == student_id).order_by(Booking.booked_at.desc()).all()
