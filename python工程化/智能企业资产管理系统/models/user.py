from datetime import datetime
from typing import TYPE_CHECKING
from sqlalchemy import Integer, String, Float, DateTime, Numeric, Column, ForeignKey, Date, Enum, Table
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from core.database import Base
if TYPE_CHECKING:
    from models.department import Department
    from models.asset_log import AssetLog
    from models.role import Role

class User(Base):
    __tablename__ = 'user'
    id:Mapped[int] = mapped_column(
        Integer,
        primary_key = True,
        autoincrement = True,
        comment = '用户唯一 ID'
    )
    username:Mapped[str] = mapped_column(
        String(50),
        nullable = False,
        unique = True,
        comment = "登录用户名"
    )
    password:Mapped[str] = mapped_column(
        String(100),
        nullable = False,
        comment = "加密存储（bcrypt）"
    )
    name:Mapped[str] = mapped_column(
        String(20),
        nullable = False,
        comment = "真实姓名"
    )
    phone:Mapped[str] = mapped_column(
        String(11),
        nullable = True,
        unique = True,
        comment = "手机号"
    )
    dept_id:Mapped[int] = mapped_column(
        ForeignKey('department.id'),
        comment = "所属部门 ID"
    )
    role_id:Mapped[str] = mapped_column(
        ForeignKey('role.id'),
        comment = "角色 ID（多角色可选扩展）"
    )
    status:Mapped[str] = mapped_column(
        Integer,
        nullable = False,
        default = 1,
        comment = "状态（0 = 禁用，1 = 正常）"
    )
    last_login:Mapped[datetime] = mapped_column(
        DateTime,
        nullable = True,
        comment = "最后登录时间"
    )
    created_time:Mapped[datetime] = mapped_column(
        DateTime,
        nullable = False,
        default = datetime.now(),
        comment = "创建时间"
    )

    department:Mapped["Department"] = relationship(
        back_populates="users"
    )

    role:Mapped["Role"] = relationship(
        back_populates="users"
    )

    assets:Mapped[list["Asset"]] = relationship(
        back_populates = "user",
        cascade = "all, delete-orphan"
    )

    asset_logs:Mapped[list["AssetLog"]] = relationship(
        back_populates = "user",
        cascade = "all, delete-orphan"
    )
