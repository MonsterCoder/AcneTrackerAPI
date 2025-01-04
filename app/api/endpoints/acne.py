from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.models import models
from app.schemas import schemas

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