from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import declarative_base

from core.setting import setting


def migrate():
    engine = create_engine(setting.DB_URI)
    metadata = MetaData()

    # Bind the engine to the metadata
    Base = declarative_base()
    Base.metadata.bind = engine
    metadata.create_all(engine)  # Create tables based on defined models
