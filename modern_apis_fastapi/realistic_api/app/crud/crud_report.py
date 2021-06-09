from typing import List
from app.db.base import Report
from sqlalchemy.orm import Session
from app.models.report_schema import ReportSchemaCreate
from datetime import datetime


class CRUD_Report:
    def __init__(self, ReportModel: Report) -> None:
        self.ReportModel = ReportModel

    def create_report(self, db: Session, report: ReportSchemaCreate) -> Report:
        location = report.location
        db_report = Report(description=report.description,
                           state=location.state,
                           city=location.city,
                           country=location.country,
                           created_date=datetime.now())
        db.add(db_report)
        db.commit()
        db.refresh(db_report)
        return db_report

    def get_list_report(self, db: Session) -> List[Report]:
        return db.query(self.ReportModel).order_by(self.ReportModel.created_date.desc()).all()

crud_report = CRUD_Report(Report)