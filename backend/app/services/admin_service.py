from typing import List, Optional

from app.models.admin import Admin
from app.services.auth_service import get_password_hash


def create_admin(db, name: str, email: str, password: str, is_superuser: bool = False) -> Admin:
    existing = db.query(Admin).filter(Admin.email == email).first()
    if existing:
        return None
    admin = Admin(
        name=name,
        email=email,
        hashed_password=get_password_hash(password),
        is_superuser=is_superuser,
    )
    db.add(admin)
    db.commit()
    db.refresh(admin)
    return admin


def get_admin(db, admin_id: int) -> Optional[Admin]:
    return db.query(Admin).filter(Admin.id == admin_id).first()


def get_admin_by_email(db, email: str) -> Optional[Admin]:
    return db.query(Admin).filter(Admin.email == email).first()


def list_admins(db) -> List[Admin]:
    return db.query(Admin).all()


def update_admin(db, admin_id: int, name: Optional[str] = None, email: Optional[str] = None, password: Optional[str] = None, is_superuser: Optional[bool] = None) -> Optional[Admin]:
    admin = db.query(Admin).filter(Admin.id == admin_id).first()
    if not admin:
        return None
    if name is not None:
        admin.name = name
    if email is not None:
        admin.email = email
    if password is not None:
        admin.hashed_password = get_password_hash(password)
    if is_superuser is not None:
        admin.is_superuser = is_superuser
    db.commit()
    db.refresh(admin)
    return admin


def delete_admin(db, admin_id: int) -> bool:
    admin = db.query(Admin).filter(Admin.id == admin_id).first()
    if not admin:
        return False
    db.delete(admin)
    db.commit()
    return True
