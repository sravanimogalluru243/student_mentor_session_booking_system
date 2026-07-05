from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.availability import Availability
from app.models.booking import Booking
from app.models.feedback import Feedback
from app.models.mentor import Mentor
from app.services.auth_service import get_password_hash


def create_mentor(db: Session, mentor_in) -> Mentor:
    existing = db.query(Mentor).filter(Mentor.email == mentor_in.email).first()
    if existing:
        raise HTTPException(status_code=409, detail="Mentor email already registered")

    mentor = Mentor(
        full_name=mentor_in.full_name,
        email=mentor_in.email,
        password=get_password_hash(mentor_in.password),
        specialization=mentor_in.specialization,
        experience=mentor_in.experience,
        bio=mentor_in.bio,
    )
    db.add(mentor)
    db.commit()
    db.refresh(mentor)
    return mentor


def get_all_mentors(db: Session) -> list[Mentor]:
    return db.query(Mentor).all()


def get_mentor_by_id(db: Session, mentor_id: int) -> Mentor:
    mentor = db.query(Mentor).filter(Mentor.id == mentor_id).first()
    if not mentor:
        raise HTTPException(status_code=404, detail="Mentor not found")
    return mentor


def update_mentor(db: Session, mentor_id: int, mentor_in) -> Mentor:
    mentor = get_mentor_by_id(db, mentor_id)
    updates = _schema_updates(mentor_in)

    if "password" in updates:
        updates["password"] = get_password_hash(updates["password"])

    for field, value in updates.items():
        setattr(mentor, field, value)

    db.commit()
    db.refresh(mentor)
    return mentor


def delete_mentor(db: Session, mentor_id: int) -> dict:
    mentor = get_mentor_by_id(db, mentor_id)
    db.delete(mentor)
    db.commit()
    return {"message": "Mentor deleted successfully"}


def add_availability(db: Session, mentor_id: int, availability_in) -> Availability:
    slot = Availability(
        mentor_id=mentor_id,
        day=availability_in.day,
        start_time=availability_in.start_time,
        end_time=availability_in.end_time,
    )
    db.add(slot)
    db.commit()
    db.refresh(slot)
    return slot


def session_requests(db: Session, mentor_id: int) -> list[Booking]:
    return db.query(Booking).filter(
        Booking.mentor_id == mentor_id,
        Booking.status == "Pending",
    ).all()


def my_sessions(db: Session, mentor_id: int) -> list[Booking]:
    return db.query(Booking).filter(Booking.mentor_id == mentor_id).all()


def feedback(db: Session, mentor_id: int) -> list[Feedback]:
    return db.query(Feedback).filter(Feedback.mentor_id == mentor_id).all()


def _schema_updates(schema) -> dict:
    if hasattr(schema, "model_dump"):
        return schema.model_dump(exclude_unset=True)
    return schema.dict(exclude_unset=True)
