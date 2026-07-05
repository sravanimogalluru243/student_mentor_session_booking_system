from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from app.config import get_settings
from app.database.connection import get_db
from app.models.admin import Admin
from app.models.mentor import Mentor
from app.models.student import Student


bearer_scheme = HTTPBearer()


def _get_token_payload(token: str) -> dict:
    settings = get_settings()
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
    except JWTError as exc:
        raise credentials_exception from exc

    if not payload.get("sub") or not payload.get("role"):
        raise credentials_exception
    return payload


def get_current_student(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
    db: Session = Depends(get_db),
) -> Student:
    token = credentials.credentials
    payload = _get_token_payload(token)
    if payload["role"] != "student":
        raise HTTPException(status_code=403, detail="Student access required")

    student = db.query(Student).filter(Student.email == payload["sub"]).first()
    if not student:
        raise HTTPException(status_code=401, detail="Student not found")
    return student


def get_current_mentor(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
    db: Session = Depends(get_db),
) -> Mentor:
    token = credentials.credentials
    payload = _get_token_payload(token)
    if payload["role"] != "mentor":
        raise HTTPException(status_code=403, detail="Mentor access required")

    mentor = db.query(Mentor).filter(Mentor.email == payload["sub"]).first()
    if not mentor:
        raise HTTPException(status_code=401, detail="Mentor not found")
    return mentor


def get_current_admin(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
    db: Session = Depends(get_db),
) -> Admin:
    token = credentials.credentials
    payload = _get_token_payload(token)
    if payload["role"] != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")

    admin = db.query(Admin).filter(Admin.email == payload["sub"]).first()
    if not admin:
        raise HTTPException(status_code=401, detail="Admin not found")
    return admin


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
    db: Session = Depends(get_db),
):
    token = credentials.credentials
    payload = _get_token_payload(token)
    email = payload["sub"]
    role = payload["role"]

    model_by_role = {
        "student": Student,
        "mentor": Mentor,
        "admin": Admin,
    }
    model = model_by_role.get(role)
    if model is None:
        raise HTTPException(status_code=401, detail="Invalid user role")

    user = db.query(model).filter(model.email == email).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user
