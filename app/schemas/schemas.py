from pydantic import BaseModel
from datetime import date
from typing import Optional

class UserBase(BaseModel):
    email: str
    full_name: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        from_attributes = True

class AcneRecordBase(BaseModel):
    date: date
    severity: int
    location: str
    notes: Optional[str] = None

class AcneRecordCreate(AcneRecordBase):
    pass

class AcneRecord(AcneRecordBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True 