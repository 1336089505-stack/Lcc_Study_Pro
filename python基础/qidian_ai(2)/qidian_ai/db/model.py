from datetime import date, datetime
from typing import Annotated

from sqlalchemy import Integer, String, Date, DateTime, Text, ForeignKey, func
from sqlalchemy.orm import DeclarativeBase, Mapped, relationship, mapped_column

int_pk    = Annotated[int, mapped_column(Integer, primary_key = True, autoincrement = True, nullable = False, comment = "ID")]
str_32    = Annotated[str, mapped_column(String(32), nullable = False)]
datetime_type = Annotated[datetime, mapped_column(DateTime, default = datetime.now, server_default=func.now(), comment = '创建时间')]#有了server_default就不要default = datetime.now()，而且类加载时就会执行。

class Base(DeclarativeBase):
    pass

class Category(Base):

    __tablename__ = "ai_category"

    id: Mapped[int_pk]
    name: Mapped[str_32]  = mapped_column(comment = "分类名称")
    emoji: Mapped[str_32] = mapped_column(comment = "分类图标")

    projects: Mapped[list["Project"]] = relationship(back_populates="category", cascade = "all, delete-orphan")

    def __repr__(self):
        return f"<Category(id={self.id}, name={self.name}, emoji={self.emoji})>"

class Project(Base):

    __tablename__ = "ai_project"

    id: Mapped[int_pk]
    name: Mapped[str] = mapped_column(String(128), nullable = False, comment = "项目名称")
    star: Mapped[int] = mapped_column(Integer, nullable = False, default =1, comment = "项目星级", index = True)
    introduction: Mapped[str] = mapped_column(String(500), nullable = True, comment = "项目简介")
    added_on: Mapped[date] = mapped_column(Date, nullable = False, default = datetime.now, comment = "收录时间", index = True) #datetime.now会将函数当参数传递给datetime.now()，而不是调用datetime.now()。
    reviews: Mapped[int] = mapped_column(Integer, nullable = False, default = 0, comment = "项目浏览数" , index = True)
    link: Mapped[str] = mapped_column(String(128), comment = "项目链接")
    detail: Mapped[str] = mapped_column(Text, comment = "项目详情")
    create_at: Mapped[datetime_type] = mapped_column(comment = "创建时间", index = True)
    update_at: Mapped[datetime_type] = mapped_column(comment = "更新时间")

    category_id: Mapped[int] = mapped_column(ForeignKey("ai_category.id"), nullable = True, comment="项目分类")
    category: Mapped[Category] = relationship(back_populates="projects")

    def __repr__(self):
        return f"<Project(id={self.id}, name={self.name}, star={self.star}, introduction={self.introduction}, added_on={self.added_on}, reviews={self.reviews}, link={self.link}, create_at={self.create_at}, update_at={self.update_at})>"