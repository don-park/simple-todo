from pydantic import BaseModel, EmailStr, constr

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: constr(min_length=8)

class UserInDB(UserBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True 