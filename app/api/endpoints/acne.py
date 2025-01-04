from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from typing import List
import base64
from openai import AzureOpenAI
from app.core.config import settings
from app.db.database import get_db
from app.models import models
from app.schemas import schemas

router = APIRouter()

def analyze_image_with_openai(base64_image) -> dict:
    client = AzureOpenAI(
        api_key="c00357ad34d741e6a870b91b8e3c3a3f",
        api_version="2024-05-01-preview",  
        azure_endpoint="https://georgecprot401261087032.openai.azure.com/"
    )

    # Convert the image to base64
    # base64_image = base64.b64encode(image_data).decode('utf-8')

    # Prepare the messages for GPT-4 Vision
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": """You are a dermatologist. You are provided a face image, scan this image for acne spots. don't miss any acne spots. Please identify severity level from 1 to 5, location of acne(cheek, forehead, chin etc), confidence score from 0 to 1. Return the results in a json format. Example  result: 
                    ```
                    {
                    "total_detected": 3,
                    "records": [
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
                    ```
                    """
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}"
                    }
                }
            ]
        }
    ]
    print(f"data:image/jpeg;base64,{base64_image}")
    try:
        # Make the API call
        response = client.chat.completions.create(
            model="gpt-4o",  # Make sure this model is available in your deployment
            messages=messages,
            max_tokens=1000,
            temperature=0.0,
            response_format={"type": "json_object"}
        )
        print(response)
        return  response.choices[0].message.content
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=f"OpenAI API error: {str(e)}")

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

@router.post("/analyze")
async def analyze_acne_image(
    image: UploadFile = File(...)
):
    # Verify that the uploaded file is an image
    if not image.content_type.startswith('image/'):
        raise HTTPException(status_code=400, detail="Uploaded file must be an image")

   # Read the image data as base64
    image_data = base64.b64encode(await image.read()).decode('utf-8')
    # add base64 metadata to the image
    # image_data = f"data:image/jpeg;base64,{image_data}"
    # image_data = await image.read()
    
    # Analyze the image using OpenAI
    analysis_result = analyze_image_with_openai(image_data)
    
   
    
    return analysis_result 