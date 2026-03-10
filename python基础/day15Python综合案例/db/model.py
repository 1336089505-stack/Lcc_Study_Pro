from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column
from sqlalchemy import create_engine, Column, Integer, String

#数据库ORM映射，并自动在数据库中创建对应的表
#定义基类
class Base(DeclarativeBase):
    pass

#定义客户模型
class Customer(Base):
    __tablename__ = 'customer'
    #id Mapped声明式 ORM 类型注解 primary_key主键
    id: Mapped[int] = mapped_column(primary_key=True)
    #name string(50)字符串50字节 nullable非空
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    #age Integer数字 可为空
    age: Mapped[int|None] = mapped_column(Integer, nullable=True)
    #phone
    phone: Mapped[str|None] = mapped_column(String(20), nullable=True)
    #email
    email: Mapped[str|None] = mapped_column(String(30), nullable=True)
