from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.booking import Booking
from app.models.feedback import Feedback
from app.models.student import Student
from app.services.auth_service import get_password_hash


def get_all_students(db: Session) -> list[Student]:
    return db.query(Student).all()


def get_student_by_id(db: Session, student_id: int) -> Student:
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


def update_student(db: Session, student_id: int, student_in) -> Student:
    student = get_student_by_id(db, student_id)
    updates = _schema_updates(student_in)
    if "password" in updates:
        updates["password"] = get_password_hash(updates["password"])

    for field, value in updates.items():
        setattr(student, field, value)

    db.commit()
    db.refresh(student)
    return student


def delete_student(db: Session, student_id: int) -> dict:
    student = get_student_by_id(db, student_id)
    db.delete(student)
    db.commit()
    return {"message": "Student deleted successfully"}


def dashboard(db: Session, student_id: int) -> dict:
    student = get_student_by_id(db, student_id)
    return {
        "student_name": student.full_name,
        "total_bookings": db.query(Booking).filter(Booking.student_id == student.id).count(),
        "completed_sessions": db.query(Booking).filter(
            Booking.student_id == student.id,
            Booking.status == "Completed",
        ).count(),
        "pending_sessions": db.query(Booking).filter(
            Booking.student_id == student.id,
            Booking.status == "Pending",
        ).count(),
    }


def my_feedback(db: Session, student_id: int) -> list[Feedback]:
    return db.query(Feedback).filter(Feedback.student_id == student_id).all()


def _schema_updates(schema) -> dict:
    if hasattr(schema, "model_dump"):
        return schema.model_dump(exclude_unset=True)
    return schema.dict(exclude_unset=True)
