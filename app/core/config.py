from pydantic_settings import BaseSettings

class Settings(BaseSettings):
  XAI_API_KEY: str
  MANAGEMENT_API_KEY: str
  COLLECTION_ID: str
  AI_MODEL: str = "grok-3"
  APP_NAME: str = "xAI Chat API"
  DEBUG: bool = True

  class Config:
    env_file = ".env"

settings = Settings()