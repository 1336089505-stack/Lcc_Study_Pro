from datetime import datetime,date
from typing import Optional

from sqlalchemy import Integer, String, Float, DateTime, Numeric, Column, ForeignKey, Date, Enum, Table, DECIMAL, \
    CheckConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass
"""
1 生鲜商品表（product） 
存储生鲜商品的基础信息，作为订单关联的核心表，字段如下：
- id：INT，主键，自增，商品唯一ID 
- name：VARCHAR(50)，非空，商品名称（如：山东烟台苹果、新鲜生菜） 
- price：DECIMAL(6,2)，非空，商品单价（单位：元/斤） 
- stock：INT，非空，商品库存（单位：斤），默认值0 
- create_time：DATETIME，非空，商品添加时间（默认当前时间） 
"""
class Product(Base):
    __tablename__ = 'product'
    id: Mapped[int] = mapped_column(Integer,
                                    primary_key=True,
                                    autoincrement=True,
                                    nullable=False,
                                    comment='商品唯一ID')

    name: Mapped[str] = mapped_column(String(50),
                                      nullable=False,
                                      comment="商品名称")
    price:Mapped[float] = mapped_column(DECIMAL(6,2),
                                        nullable=False,
                                        comment="商品单价（单位：元/斤）")
    stock:Mapped[int] = mapped_column(Integer,
                                      nullable=False,
                                      default=0,
                                      comment="商品库存（单位：斤）")
    create_time:Mapped[datetime] = mapped_column(DateTime,
                                                 nullable=False,
                                                 default=datetime.now,
                                                 comment="商品添加时间")
    order_infos:Mapped[list["OrderInfo"]] = relationship(back_populates="product",
                                                cascade = "all, delete-orphan",
                                                lazy="noload")
    def __repr__(self):
        return (f"Product id={self.id},\nname={self.name},\n"
                f"price={self.price},\nstock={self.stock},\n"
                f"create_time={self.create_time}\n")

"""
2 配送员表（deliveryman） 
存储配送员信息，用于关联订单的配送负责人，字段如下： 
- id：INT，主键，自增，配送员唯一ID 
- name：VARCHAR(20)，非空，配送员姓名 
- phone：VARCHAR(11)，非空，配送员手机号（唯一约束） 
- status：INT，非空，配送员状态（0=休息，1=在岗），默认值1 
"""
class Deliveryman(Base):
    __tablename__ = 'deliveryman'
    id: Mapped[int] = mapped_column(Integer,
                                    primary_key=True,
                                    autoincrement=True,
                                    nullable=False,
                                    comment='配送员唯一ID')
    name: Mapped[str] = mapped_column(String(20),
                                      nullable=False,
                                      comment="配送员姓名")
    phone: Mapped[str] = mapped_column(String(11),
                                       nullable=False,
                                       comment="配送员手机号")
    status:Mapped[int] = mapped_column(Integer,
                                       Enum('0', '1'),
                                       nullable=False,
                                       default=1,
                                       comment = "配送员状态")
    order_infos:Mapped[list["OrderInfo"]] = relationship(back_populates="deliveryman",
                                                cascade = "all, delete-orphan",
                                                lazy="noload")
    def __repr__(self):
        return (f"Deliveryman id={self.id},\nname={self.name},\n"
                f"phone={self.phone},\nstatus={self.status}\n")

"""
3 配送订单表（order_info） 
存储用户的生鲜配送订单信息，关联商品表和配送员表，字段如下： 
- id：INT，主键，自增，订单唯一ID 
- product_id：INT，非空，外键，关联商品表的product_id（商品ID） 
- delivery_id：INT，非空，外键，关联配送员表的delivery_id（配送员ID） 
- amount：INT，非空，订单商品数量（单位：斤），大于0 
- total：DECIMAL(8,2)，非空，订单总金额（单价×数量） 
- address：VARCHAR(100)，非空，用户配送地址 
- status：INT，非空，订单状态（0=待配送，1=配送中，2=已完成，3=已取消），默认值0 
- order_time：DATETIME，非空，订单创建时间（默认当前时间） 
"""
class OrderInfo(Base):
    __tablename__ = 'order_info'

    id: Mapped[int] = mapped_column(Integer,
                                    primary_key=True,
                                    autoincrement=True,
                                    nullable=False,
                                    comment='订单唯一ID')
    product_id:Mapped[int] = mapped_column(ForeignKey('product.id'),
                                           nullable=False,
                                           comment="商品ID")
    deliveryman_id: Mapped[int] = mapped_column(ForeignKey('deliveryman.id'),
                                            nullable=False,
                                            comment="配送员ID")
    amount: Mapped[int] = mapped_column(Integer,
                                        nullable=False,
                                        comment="订单商品数量")
    total: Mapped[float] = mapped_column(DECIMAL(8,2),
                                       nullable=False,
                                       comment="订单总金额")
    address:Mapped[str] = mapped_column(String(100),
                                        nullable=False,
                                        comment = "用户配送地址")
    status:Mapped[int] = mapped_column(Integer,
                                       Enum('0', '1', '2', '3'),
                                       nullable=False,
                                       default=0,
                                       comment="订单状态")
    order_time:Mapped[datetime] = mapped_column(DateTime,
                                                nullable=False,
                                                default=datetime.now(),
                                                comment="订单创建时间")
    product: Mapped[Product] = relationship(back_populates="order_infos",
                                              lazy="joined")
    deliveryman: Mapped[Deliveryman] = relationship(back_populates="order_infos",
                                                    lazy="joined")

    def __repr__(self):
        return (f"OrderInfo id={self.id},\namount={self.amount},\n"
                f"total={self.total},\naddress={self.address},\n"
                f"status={self.status},\norder_time={self.order_time}\n")

