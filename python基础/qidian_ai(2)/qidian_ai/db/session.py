from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from core.settings import config

engine = create_engine(
    config.DATABASE_URL,
    echo = config.DATABASE_ECHO,
    pool_size = config.DATABASE_POOL_SIZE,
    max_overflow = config.DATABASE_MAX_OVERFLOW)

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

@contextmanager
def get_session() -> Session:
    session: Session = None
    try:
        session = SessionLocal()
        yield session
        session.commit()
    except Exception as e:
        if session:
            session.rollback()
        raise e
    finally:
        if session:
            session.close()

