from datetime import datetime

from sqlalchemy import Integer, String, Float, DateTime, Numeric, Column, ForeignKey, Date, Enum, Table
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from core.database import Base
from models.user import User


class Role(Base):
    __tablename__ = "role"
    id:Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
        comment = "角色唯一 ID"
    )
    name:Mapped[str] = mapped_column(
        String(30),
        nullable = False,
        unique = True,
        comment = "角色名称（如超级管理员、资产管理员）"
    )
    desc:Mapped[str] = mapped_column(
        String(200),
        nullable = True,
        comment = "角色描述"
    )
    menu_ids:Mapped[str] = mapped_column(
        String(200),
        nullable = False,
        comment = "关联菜单 ID（逗号分隔）"
    )
    status:Mapped[int] = mapped_column(
        Integer,
        nullable = False,
        default = 1,
        comment = "状态（0 = 禁用，1 = 正常）"
    )

    users: Mapped[list["User"]] = relationship(
        back_populates="department",
        cascade="all, delete-orphan"
    )

