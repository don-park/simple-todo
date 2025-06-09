from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "SimpleToDo"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api"
    
    DB_ACCESS_URL: str
    DB_SECRET_KEY: str
    
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 days
    
    class Config:
        env_file = ".env"

settings = Settings() 