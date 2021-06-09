from logging import error
from app.models.validation_error import ValidationError
from typing import Any, Dict
import httpx
from app.core.config import settings
from app.models.location import Location
from redis import Redis
from app.cache.cache import cache_handler
from httpx import Response


async def get_report_async(cache: Redis, loc: Location, units: str) -> Dict[str, Any]:
    units = validate_units(units=units)
    if loc.state:
        q = f"{loc.city},{loc.state},{loc.country}"
    else:
        q = f"{loc.city},{loc.country}"

    if forecast := cache_handler.get_weather(cache, q):
        return forecast

    url = f"{settings.WEATHER_HOST}/data/2.5/weather?q={q}&APPID={settings.WEATHER_API_KEY}&units={units}"

    async with httpx.AsyncClient() as client:
        resp: Response = await client.get(url)
        # error handling
        if resp.status_code != 200:
            raise ValidationError(resp.text, status_code=resp.status_code)

    data: dict = resp.json()
    forecast = data["main"]

    cache_handler.set_weather(cache, q, forecast)

    return forecast


def validate_units(units: str) -> str:
    if units:
        units = units.strip().lower()
    valid_units = {'standard', 'metric', 'imperial'}
    if units not in valid_units:
        error = f"Invalid units '{units}'. It must be one of {valid_units}"
        raise ValidationError(error, status_code=400)
    return units