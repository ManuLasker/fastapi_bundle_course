from app.db.base_class import Base
from sqlalchemy import Integer, Column, String, DateTime


class Report(Base):
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    created_date = Column(DateTime, index=True)
    city = Column(String, nullable=False)
    state = Column(String, nullable=True)
    country = Column(String, nullable=True)
    description = Column(String, nullable=False)

    def __repr__(self) -> str:
        return (
            f"<Report(id: {self.id}, created_date:{self.created_date},"
            f" city:{self.city}, state:{self.state}, country:{self.country},"
            f" description: {self.description})>"
        )
