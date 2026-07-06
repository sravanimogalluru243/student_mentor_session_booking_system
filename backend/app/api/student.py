from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.dependencies import get_current_admin, get_current_student
from app.models.admin import Admin
from app.models.student import Student
from app.schemas.student import StudentRead, StudentUpdate
from app.services import student_service


router = APIRouter(prefix="/students", tags=["Students"])


@router.get("/dashboard")
def dashboard(
    db: Session = Depends(get_db),
    current_student: Student = Depends(get_current_student),
):
    return student_service.dashboard(db, current_student.id)


@router.get("/profile", response_model=StudentRead)
def get_my_profile(current_student: Student = Depends(get_current_student)):
    return current_student


@router.put("/profile", response_model=StudentRead)
def update_my_profile(
    student: StudentUpdate,
    db: Session = Depends(get_db),
    current_student: Student = Depends(get_current_student),
):
    return student_service.update_student(db, current_student.id, student)


@router.get("/", response_model=list[StudentRead])
def get_students(
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin),
):
    return student_service.get_all_students(db)


@router.get("/{student_id}", response_model=StudentRead)
def get_student(
    student_id: int,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin),
):
    return student_service.get_student_by_id(db, student_id)


@router.put("/{student_id}", response_model=StudentRead)
def update_student(
    student_id: int,
    student: StudentUpdate,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin),
):
    return student_service.update_student(db, student_id, student)


@router.delete("/{student_id}")
def delete_student(
    student_id: int,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin),
):
    return student_service.delete_student(db, student_id)
