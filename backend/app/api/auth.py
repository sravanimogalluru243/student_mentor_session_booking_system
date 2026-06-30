from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from app.database.connection import get_db
from app.services import auth_service

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
	user = auth_service.authenticate_student(db, form_data.username, form_data.password)
	if not user:
		raise HTTPException(status_code=400, detail="Incorrect username or password")
	access_token = auth_service.create_access_token({"sub": user.email})
	return {"access_token": access_token, "token_type": "bearer"}
