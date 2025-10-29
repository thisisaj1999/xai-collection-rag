from fastapi import FastAPI
from api.router.chat_router import router as chat_router
from core.config import settings

def create_app() -> FastAPI:
  app = FastAPI(title=settings.APP_NAME)
  app.include_router(chat_router)
  return app

app = create_app()