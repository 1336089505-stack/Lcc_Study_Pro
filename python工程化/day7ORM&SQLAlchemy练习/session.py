from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from contextlib import contextmanager

engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/day7_mysql')

SessionLocal = sessionmaker(
    autocommit = False, # 关闭自动提交
    autoflush = False,  # 关闭自动刷新
    bind = engine       # 绑定数据库引擎
)

@contextmanager
def get_session():
    session = None
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
