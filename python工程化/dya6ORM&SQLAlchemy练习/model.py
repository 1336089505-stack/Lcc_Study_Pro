from datetime import datetime

from sqlalchemy import Integer, String, Float, DateTime,Numeric
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

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

class Base(DeclarativeBase):
    pass

class Product(Base):
    __tablename__ = 'product'
    id:Mapped[int] = mapped_column(
        Integer,
        primary_key=True ,
        autoincrement=True,
        nullable=False,
        comment= "商品ID")
    name:Mapped[str] = mapped_column(
        String(50),
        comment= "商品名称"
    )
    price:Mapped[float] = mapped_column(
        Numeric(10, 2),
        comment= "商品价格"
    )
    stock:Mapped[int] = mapped_column(
        Integer,
        comment= "商品库存"
    )
    created_at:Mapped[datetime] = mapped_column(
        DateTime,
        comment= "创建时间"
    )

    def __repr__(self):
        return f"<Product(id={self.id}, name={self.name}, price={self.price}, stock={self.stock}, created_at={self.created_at})>"