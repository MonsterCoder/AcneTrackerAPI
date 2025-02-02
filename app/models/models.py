from sqlalchemy import Column, Integer, String, Date, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    full_name = Column(String)
    
    acne_records = relationship("AcneRecord", back_populates="user")

class AcneRecord(Base):
    __tablename__ = "acne_records"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    date = Column(Date)
    severity = Column(Integer)  # 1-5 scale
    location = Column(String)
    notes = Column(String, nullable=True)

    user = relationship("User", back_populates="acne_records") 

class AcneAnalysis(Base):
    __tablename__ = "acne_analyses"

    id = Column(Integer, primary_key=True, index=True)
    analysis_result = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now()) 