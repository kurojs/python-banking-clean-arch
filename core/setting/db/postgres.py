from sqlalchemy import create_engine


def initialize_postgres_db():
    from core.setting.setting import DB_URI
    engine = create_engine(DB_URI)
    return engine
