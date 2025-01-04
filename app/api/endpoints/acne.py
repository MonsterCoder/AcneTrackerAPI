from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.models import models
from app.schemas import schemas
from datetime import datetime

router = APIRouter()

@router.post("/", response_model=schemas.AcneRecord)
def create_acne_record(
    record: schemas.AcneRecordCreate,
    user_id: int,
    db: Session = Depends(get_db)
):
    db_record = models.AcneRecord(**record.dict(), user_id=user_id)
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record

@router.get("/{user_id}/records", response_model=List[schemas.AcneRecord])
def read_user_records(user_id: int, db: Session = Depends(get_db)):
    records = db.query(models.AcneRecord).filter(models.AcneRecord.user_id == user_id).all()
    return records 

@router.post("/analyze", response_model=schemas.AcneAnalysisResponse)
async def analyze_image(image: UploadFile = File(...)):
    # Here we'll just return dummy data
    # In a real implementation, you'd process the image and detect acne
    
    dummy_records = [
        schemas.AcneRecord(
            id=1,
            severity=3,
            location="forehead",
            confidence_score=0.89
        ),
        schemas.AcneRecord(
            id=2,
            severity=2,
            location="cheek",
            confidence_score=0.95
        ),
        schemas.AcneRecord(
            id=3,
            severity=1,
            location="chin",
            confidence_score=0.78
        )
    ]
    
    return schemas.AcneAnalysisResponse(
        total_detected=len(dummy_records),
        records=dummy_records
    ) 