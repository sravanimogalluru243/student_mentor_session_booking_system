from sqlalchemy.orm import Session

from app.models.booking import Booking
from app.models.feedback import Feedback
from app.models.mentor import Mentor
from app.models.student import Student
from app.services import mentor_service, student_service
from app.models.booking import Booking

def get_sessions(db: Session):
    return db.query(Booking).all()

def dashboard(db: Session) -> dict:
    return {
        "total_students": db.query(Student).count(),
        "total_mentors": db.query(Mentor).count(),
        "total_bookings": db.query(Booking).count(),
        "total_feedbacks": db.query(Feedback).count(),
    }


def get_students(db: Session) -> list[Student]:
    return db.query(Student).all()


def get_mentors(db: Session) -> list[Mentor]:
    return db.query(Mentor).all()


def get_bookings(db: Session) -> list[Booking]:
    return db.query(Booking).all()


def get_feedback(db: Session) -> list[Feedback]:
    return db.query(Feedback).all()


def create_mentor(db: Session, mentor):
    return mentor_service.create_mentor(db, mentor)


def update_mentor(db: Session, mentor_id: int, mentor):
    return mentor_service.update_mentor(db, mentor_id, mentor)


def delete_mentor(db: Session, mentor_id: int):
    return mentor_service.delete_mentor(db, mentor_id)


def update_student(db: Session, student_id: int, student):
    return student_service.update_student(db, student_id, student)


def delete_student(db: Session, student_id: int):
    return student_service.delete_student(db, student_id)
