from sqlalchemy.orm.session import Session
from app.models.location import Location
from typing import Generator
from redis import Redis
import redis
from app.db.session import session_local
from app.core.config import settings

def get_cache_db() -> Generator:
    try:
        # db = Redis(host=settings.REDIS_HOST)
        db = redis.from_url(url=settings.REDIS_URL)
        yield db
    finally:
        db.close()
        
def get_db() -> Generator:
    try:
        db: Session = session_local()
        yield db
    finally:
        db.close()