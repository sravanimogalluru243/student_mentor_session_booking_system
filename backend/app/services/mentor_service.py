from typing import List, Optional

from app.models.mentor import Mentor
from app.schemas.mentor import MentorCreate
from app.services.auth_service import get_password_hash


def create_mentor(db, mentor_in: MentorCreate) -> Mentor:
    mentor = Mentor(
        name=mentor_in.name,
        email=mentor_in.email,
        expertise=mentor_in.expertise,
        bio=mentor_in.bio,
        hashed_password=get_password_hash(mentor_in.password),
    )
    db.add(mentor)
    db.commit()
    db.refresh(mentor)
    return mentor


def get_mentor(db, mentor_id: int) -> Optional[Mentor]:
    return db.query(Mentor).filter(Mentor.id == mentor_id).first()


def list_mentors(db) -> List[Mentor]:
    return db.query(Mentor).all()
