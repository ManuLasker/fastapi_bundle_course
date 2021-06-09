from app.db.session import engine
from app.db import base

def init_db() -> None:
    """Function to create local metadata from db when loading app
    """
    base.Base.metadata.create_all(bind=engine)