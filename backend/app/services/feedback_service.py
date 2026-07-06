from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.booking import Booking
from app.models.feedback import Feedback


def create_feedback(db: Session, student_id: int, feedback_in) -> Feedback:
    booking = db.query(Booking).filter(
        Booking.id == feedback_in.booking_id,
        Booking.student_id == student_id,
    ).first()
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    if booking.status != "Completed":
        raise HTTPException(status_code=400, detail="Feedback is allowed after completion only")

    existing = db.query(Feedback).filter(Feedback.booking_id == booking.id).first()
    if existing:
        raise HTTPException(status_code=409, detail="Feedback already submitted for this booking")

    feedback = Feedback(
        booking_id=booking.id,
        student_id=booking.student_id,
        mentor_id=booking.mentor_id,
        rating=feedback_in.rating,
        comment=feedback_in.comment,
    )
    db.add(feedback)
    db.commit()
    db.refresh(feedback)
    return feedback


def get_student_feedback(db: Session, student_id: int) -> list[Feedback]:
    return db.query(Feedback).filter(Feedback.student_id == student_id).all()


def get_mentor_feedback(db: Session, mentor_id: int) -> list[Feedback]:
    return db.query(Feedback).filter(Feedback.mentor_id == mentor_id).all()


def get_all_feedback(db: Session) -> list[Feedback]:
    return db.query(Feedback).all()
