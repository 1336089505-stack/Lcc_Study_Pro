from datetime import datetime

from sqlalchemy import Integer, String, Float, DateTime, Numeric, Column, ForeignKey, Date, Enum, Table, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from core.database import Base
from models.asset import Asset
from models.user import User


class AssetLog(Base):
    __tablename__ = "asset_log"
    id:Mapped[int] = mapped_column(
        Integer,
        primary_key = True,
        autoincrement = True,
        comment = '日志唯一 ID'
    )
    asset_id:Mapped[int] = mapped_column(
        ForeignKey('asset.id'),
        comment = "关联资产 ID"
    )
    operate_user_id:Mapped[int] = mapped_column(
        ForeignKey('user.id'),
        comment = "操作人 ID"
    )
    operate_type:Mapped[str] = mapped_column(
        String(20),
        Enum("新增", "修改", "领用", "归还", "维修", "报废"),
        nullable = False,
        comment = "操作类型"
    )
    old_date:Mapped[str] = mapped_column(
        Text,
        nullable = True,
        comment = "操作前数据（JSON 格式）"
    )
    new_data:Mapped[str] = mapped_column(
        Text,
        nullable = True,
        comment = "操作后数据（JSON 格式）"
    )
    operate_time:Mapped[datetime] = mapped_column(
        DateTime,
        nullable = False,
        default = datetime.now(),
        comment = "操作时间"
    )
    remark:Mapped[str] = mapped_column(
        String(500),
        nullable = True,
        comment = "操作备注"
    )

    asset:Mapped[Asset] = relationship(
        back_populates="asset_logs"
    )

    user:Mapped[User] = relationship(
        back_populates="asset_logs"
    )