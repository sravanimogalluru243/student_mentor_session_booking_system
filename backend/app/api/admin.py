from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.dependencies import get_current_admin
from app.models.admin import Admin

from app.schemas.admin import DashboardResponse
from app.schemas.booking import BookingResponse
from app.schemas.feedback import FeedbackResponse
from app.schemas.mentor import MentorCreate, MentorRead, MentorUpdate
from app.schemas.student import StudentRead, StudentUpdate
from app.schemas.session import SessionRead

from app.services import admin_service

router = APIRouter(prefix="/admin", tags=["Admin"])


# ================= Dashboard =================

@router.get("/dashboard", response_model=DashboardResponse)
def dashboard(
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin),
):
    return admin_service.dashboard(db)


# ================= Students =================

@router.get("/students", response_model=list[StudentRead])
def get_students(
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin),
):
    return admin_service.get_students(db)


@router.put("/students/{student_id}", response_model=StudentRead)
def update_student(
    student_id: int,
    student: StudentUpdate,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin),
):
    return admin_service.update_student(db, student_id, student)


@router.delete("/students/{student_id}")
def delete_student(
    student_id: int,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin),
):
    return admin_service.delete_student(db, student_id)


# ================= Mentors =================

@router.get("/mentors", response_model=list[MentorRead])
def get_mentors(
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin),
):
    return admin_service.get_mentors(db)


@router.post("/mentors", response_model=MentorRead)
def create_mentor(
    mentor: MentorCreate,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin),
):
    return admin_service.create_mentor(db, mentor)


@router.put("/mentors/{mentor_id}", response_model=MentorRead)
def update_mentor(
    mentor_id: int,
    mentor: MentorUpdate,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin),
):
    return admin_service.update_mentor(db, mentor_id, mentor)


@router.delete("/mentors/{mentor_id}")
def delete_mentor(
    mentor_id: int,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin),
):
    return admin_service.delete_mentor(db, mentor_id)


# ================= Sessions =================

@router.get("/sessions", response_model=list[SessionRead])
def get_sessions(
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin),
):
    return admin_service.get_sessions(db)


# ================= Bookings =================

@router.get("/bookings", response_model=list[BookingResponse])
def get_bookings(
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin),
):
    return admin_service.get_bookings(db)


# ================= Feedback =================

@router.get("/feedback", response_model=list[FeedbackResponse])
def get_feedback(
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin),
):
    return admin_service.get_feedback(db)