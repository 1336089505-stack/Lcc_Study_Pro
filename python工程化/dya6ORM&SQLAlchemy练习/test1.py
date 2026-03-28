"""
设计一个商品实体类Product，要求如下：
1. 	包含以下属性：id（主键，自增）、name（商品名称）、
price（价格，小数位2位）、stock（库存）、created_at（创建时间）
2. 	使用SQLAlchemy实现
3. 	编写代码实现以下功能：
	创建Product表
	插入3条商品记录
	根据id查询单个商品
	查询所有商品并按创建时间降序排列
"""
from datetime import datetime

from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker,Session
from model import Base,Product

engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/day6_mysql')

Base.metadata.create_all(engine)

SessionLocal = sessionmaker(
    autocommit = False, # 关闭自动提交
    autoflush = False,  # 关闭自动刷新
    bind = engine       # 绑定数据库引擎
)

session = SessionLocal()

pro = [
    Product(name = "手机",
            price = 2000.00,
            stock = 30,
            created_at = datetime.now(),
            ),
    Product(name="手表",
            price=1000.00,
            stock=20,
            created_at=datetime.now(),
            ),
    Product(name="电脑",
            price=3000.00,
            stock=60,
            created_at=datetime.now(),
            )
]
session.add_all(pro)
session.commit()


def find_by_id(product_id:int):
    state = select(Product).where(Product.id == product_id)
    result = session.execute(state)
    product = result.scalars().one_or_none()
    return product

def find_all():
    state = select(Product).order_by(Product.created_at.desc())
    result = session.scalars(state)
    categories = result.all()
    return categories

pro = find_by_id(19)
pro_list = find_all()
print(pro)
for i in pro_list:
    print(i)

session.close()


