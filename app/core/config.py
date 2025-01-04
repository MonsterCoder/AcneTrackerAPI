from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Acne Tracker"
    OPENAI_API_BASE: str = "https://georgecprot401261087032.openai.azure.com/"
    OPENAI_API_KEY: str = "c00357ad34d741e6a870b91b8e3c3a3f"
    OPENAI_API_VERSION: str = "2024-02-15-preview"  # Use the latest API version
    
    class Config:
        case_sensitive = True

settings = Settings() 