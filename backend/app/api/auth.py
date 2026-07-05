from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.dependencies import get_current_user
from app.schemas.student import StudentCreate, StudentRead
from app.services import auth_service


router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/student/register", response_model=StudentRead)
def register_student(student: StudentCreate, db: Session = Depends(get_db)):
    return auth_service.register_student(db, student)


@router.post("/student/login")
def student_login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    student = auth_service.authenticate_student(db, form_data.username, form_data.password)
    if not student:
        raise HTTPException(status_code=400, detail="Invalid email or password")

    token = auth_service.create_access_token({"sub": student.email, "role": "student"})
    return {
        "access_token": token,
        "token_type": "bearer",
        "role": "student",
        "user_id": student.id,
        "full_name": student.full_name,
    }


@router.post("/mentor/login")
def mentor_login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    mentor = auth_service.authenticate_mentor(db, form_data.username, form_data.password)
    if not mentor:
        raise HTTPException(status_code=400, detail="Invalid email or password")

    token = auth_service.create_access_token({"sub": mentor.email, "role": "mentor"})
    return {
        "access_token": token,
        "token_type": "bearer",
        "role": "mentor",
        "user_id": mentor.id,
        "full_name": mentor.full_name,
    }


@router.post("/admin/login")
def admin_login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    admin = auth_service.authenticate_admin(db, form_data.username, form_data.password)
    if not admin:
        raise HTTPException(status_code=400, detail="Invalid email or password")

    token = auth_service.create_access_token({"sub": admin.email, "role": "admin"})
    return {
        "access_token": token,
        "token_type": "bearer",
        "role": "admin",
        "user_id": admin.id,
        "full_name": admin.full_name,
    }


@router.get("/me")
def get_profile(current_user=Depends(get_current_user)):
    return {
        "id": current_user.id,
        "full_name": current_user.full_name,
        "email": current_user.email,
        "role": current_user.__tablename__.removesuffix("s"),
    }


@router.post("/logout")
def logout():
    return {"message": "Logged out successfully"}
