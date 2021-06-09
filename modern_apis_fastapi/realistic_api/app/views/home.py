from app.models import report
from fastapi.params import Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi import APIRouter
from fastapi import Request
from app.app import templates
from sqlalchemy.orm import Session
from app.cache.deps import get_db
from app.crud.crud_report import crud_report

router = APIRouter()

@router.get("/", response_class=HTMLResponse, include_in_schema=False)
def index(request: Request, db: Session = Depends(get_db)):
    reports = crud_report.get_list_report(db)
    return templates.TemplateResponse(name="home/index.html",
                               context={"request": request, "events": reports})
    
@router.get("/favicon.ico", include_in_schema=False)
def favicon():
    return RedirectResponse(url="/static/img/favicon.ico")