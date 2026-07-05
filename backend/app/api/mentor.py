from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.dependencies import get_current_admin, get_current_mentor
from app.models.admin import Admin
from app.models.mentor import Mentor
from app.schemas.booking import BookingResponse
from app.schemas.feedback import FeedbackResponse
from app.schemas.mentor import AvailabilityCreate, AvailabilityRead, MentorCreate, MentorRead, MentorUpdate
from app.services import booking_service, mentor_service


router = APIRouter(prefix="/mentors", tags=["Mentors"])


@router.get("/", response_model=list[MentorRead])
def get_all_mentors(db: Session = Depends(get_db)):
    return mentor_service.get_all_mentors(db)


@router.get("/profile", response_model=MentorRead)
def get_my_profile(current_mentor: Mentor = Depends(get_current_mentor)):
    return current_mentor


@router.put("/profile", response_model=MentorRead)
def update_my_profile(
    mentor: MentorUpdate,
    db: Session = Depends(get_db),
    current_mentor: Mentor = Depends(get_current_mentor),
):
    return mentor_service.update_mentor(db, current_mentor.id, mentor)


@router.post("/availability", response_model=AvailabilityRead)
def add_availability(
    availability: AvailabilityCreate,
    db: Session = Depends(get_db),
    current_mentor: Mentor = Depends(get_current_mentor),
):
    return mentor_service.add_availability(db, current_mentor.id, availability)


@router.get("/requests", response_model=list[BookingResponse])
def get_session_requests(
    db: Session = Depends(get_db),
    current_mentor: Mentor = Depends(get_current_mentor),
):
    return mentor_service.session_requests(db, current_mentor.id)


@router.get("/sessions", response_model=list[BookingResponse])
def get_my_sessions(
    db: Session = Depends(get_db),
    current_mentor: Mentor = Depends(get_current_mentor),
):
    return mentor_service.my_sessions(db, current_mentor.id)


@router.patch("/bookings/{booking_id}/accept", response_model=BookingResponse)
def accept_booking(
    booking_id: int,
    db: Session = Depends(get_db),
    current_mentor: Mentor = Depends(get_current_mentor),
):
    return booking_service.mentor_update_booking_status(
        db,
        current_mentor.id,
        booking_id,
        "Accepted",
    )


@router.patch("/bookings/{booking_id}/reject", response_model=BookingResponse)
def reject_booking(
    booking_id: int,
    db: Session = Depends(get_db),
    current_mentor: Mentor = Depends(get_current_mentor),
):
    return booking_service.mentor_update_booking_status(
        db,
        current_mentor.id,
        booking_id,
        "Rejected",
    )


@router.patch("/bookings/{booking_id}/complete", response_model=BookingResponse)
def complete_booking(
    booking_id: int,
    db: Session = Depends(get_db),
    current_mentor: Mentor = Depends(get_current_mentor),
):
    return booking_service.mentor_update_booking_status(
        db,
        current_mentor.id,
        booking_id,
        "Completed",
    )


@router.get("/feedback", response_model=list[FeedbackResponse])
def get_my_feedback(
    db: Session = Depends(get_db),
    current_mentor: Mentor = Depends(get_current_mentor),
):
    return mentor_service.feedback(db, current_mentor.id)


@router.post("/", response_model=MentorRead)
def create_mentor(
    mentor: MentorCreate,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin),
):
    return mentor_service.create_mentor(db, mentor)


@router.get("/{mentor_id}", response_model=MentorRead)
def get_mentor(mentor_id: int, db: Session = Depends(get_db)):
    return mentor_service.get_mentor_by_id(db, mentor_id)


@router.put("/{mentor_id}", response_model=MentorRead)
def update_mentor(
    mentor_id: int,
    mentor: MentorUpdate,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin),
):
    return mentor_service.update_mentor(db, mentor_id, mentor)


@router.delete("/{mentor_id}")
def delete_mentor(
    mentor_id: int,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin),
):
    return mentor_service.delete_mentor(db, mentor_id)
