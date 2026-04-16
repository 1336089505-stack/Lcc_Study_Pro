from typing import TYPE_CHECKING
from datetime import datetime, date
from sqlalchemy import Integer, String, DECIMAL, Column, ForeignKey, Date, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from core.database import Base

if TYPE_CHECKING:
    from models.department import Department
    from models.user import User
    from models.asset_category import AssetCategory
    from models.asset_log import AssetLog


class Asset(Base):
    __tablename__ = 'asset'

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
        comment='资产唯一 ID'
    )
    asset_code: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        unique=True,
        comment="资产编码（自动生成，如 ASSET-20240501001）"
    )
    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        comment="资产名称（如联想笔记本电脑）"
    )
    category_id: Mapped[int] = mapped_column(
        ForeignKey('asset_category.id'),
        comment="资产分类 ID"
    )
    spec: Mapped[str] = mapped_column(
        String(200),
        nullable=True,
        comment="资产规格（如 i7-12700H、16G 内存）"
    )
    price: Mapped[float] = mapped_column(
        DECIMAL(10, 2),
        nullable=False,
        comment="资产单价"
    )
    buy_time: Mapped[date] = mapped_column(  # 你写的 but_time → 改成 buy_time
        Date,
        nullable=False,
        comment="采购时间"
    )
    use_dept_id: Mapped[int] = mapped_column(
        ForeignKey('department.id'),
        comment="使用部门 ID"
    )
    use_user_id: Mapped[int] = mapped_column(
        ForeignKey('user.id'),
        comment="使用人 ID"
    )
    status: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=1,
        comment="状态（0 = 闲置，1 = 在用，2 = 维修，3 = 报废，4 = 借用）"
    )
    expire_time: Mapped[date] = mapped_column(
        Date,
        nullable=True,
        comment="报废 / 到期时间"
    )
    supplier: Mapped[str] = mapped_column(
        String(100),
        nullable=True,
        comment="供应商名称"
    )
    create_date: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=datetime.now,
        comment="创建时间"
    )
    update_date: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=datetime.now,
        onupdate=datetime.now,
        comment="更新时间"
    )

    # ===============================
    # 关键：全部用 字符串！不要导入！
    # ===============================
    department: Mapped["Department"] = relationship(
        back_populates="assets"
    )
    user: Mapped["User"] = relationship(
        back_populates="assets"
    )
    asset_category: Mapped["AssetCategory"] = relationship(
        back_populates="assets"
    )
    asset_logs: Mapped[list["AssetLog"]] = relationship(
        back_populates="asset",
        cascade="all, delete-orphan"
    )