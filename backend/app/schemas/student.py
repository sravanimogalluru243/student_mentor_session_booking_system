from pydantic import BaseModel, EmailStr


class StudentBase(BaseModel):
    name: str
    email: EmailStr


class StudentCreate(StudentBase):
    password: str


class StudentRead(StudentBase):
    id: int

    class Config:
        from_attributes = True


class PasswordChangeRequest(BaseModel):
    old_password: str
    new_password: str
