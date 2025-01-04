from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints import acne, users
from app.core.config import settings

import uvicorn
app = FastAPI(
    title="Acne Tracker API",
    description="API for tracking acne patterns and treatments",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(users.router, prefix="/api/users", tags=["users"])
app.include_router(acne.router, prefix="/api/acne", tags=["acne"])

@app.get("/")
async def root():
    return {"message": "Welcome to Acne Tracker API"} 

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)