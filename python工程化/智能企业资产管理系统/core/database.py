# 数据库连接（连接池、自动建表、迁移）
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from contextlib import contextmanager

engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/eams')

Base = declarative_base()

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