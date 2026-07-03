from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session

from app.schemas.mentor import MentorCreate, MentorRead
from app.database.connection import get_db
from app.services import mentor_service

router = APIRouter(prefix="/mentors", tags=["mentors"])


@router.post("/", response_model=MentorRead)
def create_mentor(mentor_in: MentorCreate, db: Session = Depends(get_db)):
	return mentor_service.create_mentor(db, mentor_in)


@router.get("/", response_model=List[MentorRead])
def list_mentors(db: Session = Depends(get_db)):
	return mentor_service.list_mentors(db)

