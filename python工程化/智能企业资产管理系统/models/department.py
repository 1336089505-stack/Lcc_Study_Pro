from datetime import datetime

from sqlalchemy import Integer, String, Float, DateTime, Numeric, Column, ForeignKey, Date, Enum, Table
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from core.database import Base
from models.user import User
from models.asset import Asset


class Department(Base):
    __tablename__ = 'department'
    id:Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
        comment="部门唯一 ID"
    )
    name:Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        unique=True,
        comment="部门名称"
    )
    parent_id:Mapped[int] = mapped_column(
        ForeignKey('department.id'),
        nullable=True,
        comment="父部门 ID（支持多级部门）"
    )
    status:Mapped[int] = mapped_column(
        Integer,
        default=1,
        nullable=False,
        comment="状态（0 = 禁用，1 = 正常）"
    )
    create_date:Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=datetime.now(),
        comment="创建时间"
    )
    update_date:Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=datetime.now(),
        comment="更新时间"
    )

    children = relationship(
        "Department",
        backref="parent",
        remote_side=[id]#指定父级
    )

    users:Mapped[list["User"]] = relationship(
        back_populates = "department",
        cascade = "all, delete-orphan"
    )

    assets:Mapped[list["Asset"]] = relationship(
        back_populates = "department",
        cascade = "all, delete-orphan"
    )


