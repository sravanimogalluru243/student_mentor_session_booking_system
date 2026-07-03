from pydantic import BaseModel, EmailStr
from typing import Optional


class AdminBase(BaseModel):
    name: str
    email: EmailStr


class AdminCreate(AdminBase):
    password: str
    is_superuser: Optional[bool] = False


class AdminUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    is_superuser: Optional[bool] = None


class AdminRead(AdminBase):
    id: int
    is_superuser: bool

    class Config:
        from_attributes = True
