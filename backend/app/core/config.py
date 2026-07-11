from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    APP_NAME: str = "AI Software Engineering Assistant"
    APP_VERSION: str = "1.0.0"

    GEMINI_API_KEY: str = ""

    DATABASE_URL: str = ""

    class Config:
        env_file = ".env"


settings = Settings()