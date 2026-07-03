from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models.admin import Admin
from app.services.auth_service import get_password_hash

router = APIRouter(prefix="/admin", tags=["admin"])


@router.get("/")
def list_admins(db: Session = Depends(get_db)):
    admins = db.query(Admin).all()
    return [{"id": a.id, "name": a.name, "email": a.email, "is_superuser": a.is_superuser} for a in admins]


@router.get("/{admin_id}")
def get_admin(admin_id: int, db: Session = Depends(get_db)):
    admin = db.query(Admin).filter(Admin.id == admin_id).first()
    if not admin:
        raise HTTPException(status_code=404, detail="Admin not found")
    return {"id": admin.id, "name": admin.name, "email": admin.email, "is_superuser": admin.is_superuser}


@router.put("/{admin_id}")
def update_admin(admin_id: int, name: str | None = None, email: str | None = None, password: str | None = None, is_superuser: bool | None = None, db: Session = Depends(get_db)):
    admin = db.query(Admin).filter(Admin.id == admin_id).first()
    if not admin:
        raise HTTPException(status_code=404, detail="Admin not found")
    if name is not None:
        admin.name = name
    if email is not None:
        # ensure unique
        existing = db.query(Admin).filter(Admin.email == email, Admin.id != admin_id).first()
        if existing:
            raise HTTPException(status_code=400, detail="Email already in use")
        admin.email = email
    if password is not None:
        admin.hashed_password = get_password_hash(password)
    if is_superuser is not None:
        admin.is_superuser = is_superuser
    db.commit()
    db.refresh(admin)
    return {"id": admin.id, "name": admin.name, "email": admin.email, "is_superuser": admin.is_superuser}


@router.delete("/{admin_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_admin(admin_id: int, db: Session = Depends(get_db)):
    admin = db.query(Admin).filter(Admin.id == admin_id).first()
    if not admin:
        raise HTTPException(status_code=404, detail="Admin not found")
    db.delete(admin)
    db.commit()
    return None
