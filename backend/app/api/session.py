from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session

from app.schemas.session import SessionCreate, SessionRead, SessionUpdate
from app.database.connection import get_db
from app.services import session_service

router = APIRouter(prefix="/sessions", tags=["sessions"])


@router.post("/", response_model=SessionRead)
def create_session(session_in: SessionCreate, db: Session = Depends(get_db)):
	return session_service.create_session(db, session_in)


@router.get("/", response_model=List[SessionRead])
def list_sessions(mentor_id: int = None, db: Session = Depends(get_db)):
	return session_service.list_sessions(db, mentor_id=mentor_id)


@router.put("/{session_id}", response_model=SessionRead)
def update_session(session_id: int, session_in: SessionUpdate, db: Session = Depends(get_db)):
	updated = session_service.update_session(db, session_id, session_in)
	if not updated:
		raise HTTPException(status_code=404, detail="Session not found")
	return updated
