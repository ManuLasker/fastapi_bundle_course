from typing import Optional
from pydantic import BaseModel, validator
from fastapi import HTTPException


class Location(BaseModel):
    city: str
    state: Optional[str] = None
    country: str = "US"

    @validator("city")
    def validate_city(cls, city: str) -> str:
        city = city.strip().lower()
        return city

    @validator("state")
    def validate_state(cls, state: Optional[str]) -> Optional[str]:
        if state:
            state = state.strip().lower()
            if len(state) != 2:
                error = (
                    f"Invalid state: {state}. It must be a two letter"
                    " abbreviation such as CA or KS (use for US only)"
                )
                raise HTTPException(status_code=400, detail=error)
        return state

    @validator("country")
    def validate_country(cls, country: Optional[str]) -> str:
        if not country:
            country = "us"
        else:
            country = country.strip().lower()
            if len(country) != 2:
                error = (
                    f"Invalid country: {country}. It must be a two letter"
                    " abbreviation such as US or GB."
                )
                raise HTTPException(status_code=400, detail=error)
        return country