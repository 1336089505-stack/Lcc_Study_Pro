from datetime import date, datetime
from typing import Annotated

from sqlalchemy import Integer, String, Date, DateTime, Text, ForeignKey, func, JSON, Float,Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, relationship, mapped_column

int_pk    = Annotated[int, mapped_column(Integer, primary_key = True, autoincrement = True, nullable = False, comment = "ID")]

class Base(DeclarativeBase):
    pass

class Book(Base):

    __tablename__ = "ai_category"

    id: Mapped[int_pk]
    name: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
        comment="书籍名称"
    )
    category: Mapped[str] = mapped_column(
        String(500),
        nullable = False,
        comment="书籍分类"
    )

    binding: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
        comment="书籍装帧"
    )
    tags: Mapped[list[str]] = mapped_column(
        JSON,
        default=list,
        comment="书籍标签"
    )
    price: Mapped[float] = mapped_column(
        Float,
        nullable=False,
        comment="书籍价格"
    )
    is_sale: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        comment="书籍价格"
    )


    def __repr__(self):
        return (f"<Book(id={self.id}, name={self.name},"
                f"category={self.category},binding={self.binding},tags={self.tags},"
                f"price={self.price},is_sale={self.is_sale})>\n")

