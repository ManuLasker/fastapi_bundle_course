from typing import Any, Dict, Optional
from redis import Redis
import json
from app.core.config import settings
from datetime import timedelta


class CacheHandler:
    def set_weather(self, cache: Redis, q: str, forecast: Dict[str, Any]):
        # set with expiration time
        cache.setex(
            name=q.strip().lower(),
            time=timedelta(hours=settings.CACHE_LIFETIME_IN_HOURS),
            value=json.dumps(forecast),
        )
        
    def get_weather(self, cache:Redis, q:str) -> Optional[Dict[str, Any]]:
        forecast = cache.get(name=q.strip().lower())
        if forecast:
            forecast = json.loads(forecast)
        return forecast


cache_handler = CacheHandler()
