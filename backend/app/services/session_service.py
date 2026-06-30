from typing import List, Optional

from app.models.session import Session as SessionModel
from app.schemas.session import SessionCreate, SessionUpdate


def create_session(db, session_in: SessionCreate) -> SessionModel:
    session = SessionModel(**session_in.dict())
    db.add(session)
    db.commit()
    db.refresh(session)
    return session


def get_session(db, session_id: int) -> Optional[SessionModel]:
    return db.query(SessionModel).filter(SessionModel.id == session_id).first()


def list_sessions(db, mentor_id: int = None) -> List[SessionModel]:
    query = db.query(SessionModel)
    if mentor_id is not None:
        query = query.filter(SessionModel.mentor_id == mentor_id)
    return query.all()


def update_session(db, session_id: int, session_in: SessionUpdate) -> Optional[SessionModel]:
    session = get_session(db, session_id)
    if not session:
        return None
    for field, value in session_in.dict(exclude_unset=True).items():
        setattr(session, field, value)
    db.commit()
    db.refresh(session)
    return session
