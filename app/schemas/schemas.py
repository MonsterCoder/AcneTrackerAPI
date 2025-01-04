from pydantic import BaseModel
from datetime import date
from typing import Optional, List

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

class AcneRecord(BaseModel):
    id: int
    severity: int
    location: str
    detected_at: date
    confidence_score: float

class AcneAnalysisResponse(BaseModel):
    total_detected: int
    records: List[AcneRecord] 