from fastapi import FastAPI
from app.core.config import settings
from app.api.v1.api import api_router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

app.include_router(
    api_router,
    prefix="/api/v1"
)


@app.get("/")
def home():
    return {
       # "api_key_loaded": bool(settings.GEMINI_API_KEY)
        "app_name": settings.APP_NAME,
        "version": settings.APP_VERSION
    }