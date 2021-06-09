from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# This will create the engine database with pre ping to ping in case the connection was closed
engine = create_engine(settings.SQLALCHEMY_SQLITE_DATABASE_URI,
                       pool_pre_ping=True, connect_args={"check_same_thread": True})
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)