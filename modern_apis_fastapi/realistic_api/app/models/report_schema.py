from app.models.location import Location
from pydantic import BaseModel
from datetime import datetime

class ReportSchemaBase(BaseModel):
    description: str

class ReportSchemaCreate(ReportSchemaBase):
    location: Location
    
class ReportSchemaInDBBase(ReportSchemaBase):
    created_date: datetime
    location: Location
    
    class Config:
        orm_mode = True

class Report(ReportSchemaInDBBase):
    pass

class ReportInDB(ReportSchemaInDBBase):
    id: int