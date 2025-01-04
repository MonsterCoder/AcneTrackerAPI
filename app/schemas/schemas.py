from pydantic import BaseModel
from datetime import date
from typing import Optional, List
from datetime import datetime

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
    confidence_score: float

class AcneAnalysisResponse(BaseModel):
    total_detected: int
    records: List[AcneRecord] 

class AcneAnalysis(BaseModel):
    id: int
    analysis_result: str
    created_at: datetime
    
    class Config:
        from_attributes = True 