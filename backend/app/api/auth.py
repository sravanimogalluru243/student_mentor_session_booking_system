from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from app.database.connection import get_db
from app.services import auth_service
from app.dependencies import get_current_user
from app.models.student import Student
from app.schemas.student import StudentRead
from app.schemas.student import PasswordChangeRequest
from app.dependencies import get_current_user
from app.models.student import Student
from app.schemas.student import StudentCreate, StudentRead

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=StudentRead)
def register(student: StudentCreate, db: Session = Depends(get_db)):
    return auth_service.register_student(db, student)

@router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
	user = auth_service.authenticate_student(db, form_data.username, form_data.password)
	if not user:
		raise HTTPException(status_code=400, detail="Incorrect username or password")
	access_token = auth_service.create_access_token({"sub": user.email})
	return {"access_token": access_token, "token_type": "bearer"}

@router.get("/profile", response_model=StudentRead)
def get_profile(current_user: Student = Depends(get_current_user)):
    return current_user

@router.put("/change-password")
def change_password(
    password_data: PasswordChangeRequest,
    current_user: Student = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    auth_service.change_password(
        db,
        current_user,
        password_data.old_password,
        password_data.new_password,
    )

    return {"message": "Password changed successfully"}