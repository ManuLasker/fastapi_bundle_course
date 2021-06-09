from pydantic import BaseSettings
from pydantic import AnyUrl
import secrets

class Settings(BaseSettings):
    WEATHER_API_KEY: str
    WEATHER_HOST: AnyUrl
    STARTUP_EVENT_NAME: str = "startup"
    SHUTDOWN_EVENT_NAME: str = "shutdown"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    REDIS_URL: str
    CACHE_LIFETIME_IN_HOURS: float = 0.05
    SQLALCHEMY_SQLITE_DATABASE_URI: str

settings = Settings()