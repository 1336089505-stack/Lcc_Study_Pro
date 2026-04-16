from datetime import datetime

from sqlalchemy import Integer, String, Float, DateTime, Numeric, Column, ForeignKey, Date, Enum, Table
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from core.database import Base
from models.asset import Asset


class AssetCategory(Base):
    __tablename__ = 'asset_category'
    id:Mapped[int] = mapped_column(
        Integer,
        primary_key = True,
        autoincrement = True,
        comment = '分类唯一 ID',
    )
    name:Mapped[str] = mapped_column(
        String(50),
        nullable = False,
        comment = "分类名称（如办公设备、IT 设备）"
    )
    parent_id:Mapped[int] = mapped_column(
        ForeignKey('asset_category.id'),
        nullable = True,
        comment = "父分类 ID（支持多级分类）"
    )
    code:Mapped[str] = mapped_column(
        String(20),
        nullable = False,
        unique = True,
        comment = "分类编码（如 IT-001）"
    )
    desc:Mapped[str] = mapped_column(
        String(200),
        nullable = True,
        comment = "分类描述"
    )

    children = relationship(
        "AssetCategory",
        backref="parent",
        remote_side=[id]#指定父级
    )

    assets:Mapped[list["Asset"]] = relationship(
        back_populates = "asset_category",
        cascade = "all, delete-orphan"
    )

