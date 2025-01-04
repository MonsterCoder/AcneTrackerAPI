from fastapi import FastAPI
from app.api.endpoints import acne, users
from app.core.config import settings

app = FastAPI(
    title="Acne Tracker API",
    description="API for tracking acne patterns and treatments",
    version="1.0.0"
)

# Include routers
app.include_router(users.router, prefix="/api/users", tags=["users"])
app.include_router(acne.router, prefix="/api/acne", tags=["acne"])

@app.get("/")
async def root():
    return {"message": "Welcome to Acne Tracker API"} 