from sqlalchemy.orm import Session
from app.models.validation_error import ValidationError
from app.cache.deps import get_cache_db, get_db
from app.services.weather_service import get_report_async
from typing import Dict, List, Optional
from fastapi import APIRouter, Response
from fastapi.params import Depends
from app.models.location import Location
from app.models.report_schema import Report, ReportSchemaCreate
from app.crud.crud_report import crud_report
from redis import Redis

router = APIRouter()


@router.get("/api/weather/{city}")
async def weather(
    cache: Redis = Depends(get_cache_db),
    loc: Location = Depends(),
    units: Optional[str] = "metric",
):
    try:
        return await get_report_async(cache, loc, units=units)
    except ValidationError as ve:
        return Response(content=ve.error_msg, status_code=ve.status_code)


@router.get(
    "/api/reports", name="all_reports", response_model=Dict[str, Optional[List[Report]]]
)
def get_reports_list(db: Session = Depends(get_db)):
    # sqlite database does not support async and await

    reports = crud_report.get_list_report(db)
    reports_response = [
        Report(
            description=report.description,
            created_date=report.created_date,
            location=Location(
                city=report.city, state=report.state, country=report.country
            ),
        )
        for report in reports
    ]
    return {"reports": reports_response}


@router.post("/api/report", name="add_report", status_code=201, response_model=Report)
def create_report(new_report: ReportSchemaCreate, db: Session = Depends(get_db)):
    # sqlite database does not support async and await
    report = crud_report.create_report(db, new_report)
    report_response = Report(
        description=report.description,
        created_date=report.created_date,
        location=Location(city=report.city, state=report.state, country=report.country),
    )
    return report_response
