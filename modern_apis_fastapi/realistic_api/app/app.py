from fastapi import FastAPI
from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
from app.api import weather_api
from app.core.config import settings
from app.db.init_db import init_db

templates = Jinja2Templates(directory="templates")

from app.views import home

def get_app() -> FastAPI:
    api = FastAPI(title="Weather API!")
    api.add_event_handler(settings.STARTUP_EVENT_NAME, init_db)
    api.mount("/static", StaticFiles(directory="static"), name="static")    
    api.include_router(home.router, tags=["views"])
    api.include_router(weather_api.router, tags=["weather_api"])
    return api

api = get_app()

