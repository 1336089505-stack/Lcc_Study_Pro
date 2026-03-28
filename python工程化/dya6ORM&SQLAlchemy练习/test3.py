"""
本题基于前一作业的电商系统，使用SQLAlchemy引擎和连接查询商品表：
1、创建SQLAlchemy引擎
2、获取连接
3、查询商品表所有记录
4、善后处理
"""
from sqlalchemy import create_engine, select, MetaData
from sqlalchemy.orm import sessionmaker

from model import Base,Product

engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/day6_mysql')

SessionLocal = sessionmaker(
    autocommit = False, # 关闭自动提交
    autoflush = False,  # 关闭自动刷新
    bind = engine       # 绑定数据库引擎
)

session = None
try:
    session = SessionLocal()
    state = select(Product)
    result = session.scalars(state)
    categories = result.all()
except Exception as e:
    if session:
        session.rollback()
    raise e
finally:
    if session:
        session.close()
