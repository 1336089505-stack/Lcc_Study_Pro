
from datetime import datetime

from sqlalchemy import Integer, String, Float, DateTime, Numeric, Column, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass

class Category(Base):
    __tablename__ = 'category'
    id: Mapped[int] = mapped_column(Integer,
                                    primary_key=True,
                                    autoincrement=True,
                                    nullable=False,
                                    comment='博客分类ID')
    name: Mapped[str] = mapped_column(String(50),
                                      comment="分类名称")
    description:Mapped[str] = mapped_column(String(500),
                                            comment = "分类描述")
    created_at: Mapped[datetime] = mapped_column(DateTime,
                                                 default=datetime.now(),
                                                 comment="创建时间")
    articles:Mapped[list["Article"]] = relationship(back_populates="category",
                                                    cascade = "all, delete-orphan",
                                                    lazy="noload")
    def __repr__(self):
        return (f"Category id={self.id},\nname={self.name},\n"
                f"description={self.description},\ncreated_at={self.created_at}\n")



class Article(Base):
    __tablename__ = 'article'
    id:Mapped[int] = mapped_column(Integer,
                            primary_key = True,
                            autoincrement = True,
                            nullable = False,
                            comment = '文章ID')
    title:Mapped[str] = mapped_column(String(50),
                               comment = "文章标题")
    content:Mapped[str] = mapped_column(String(500),
                                 comment = "内容")
    created_at:Mapped[datetime] = mapped_column(DateTime,
                                                default=datetime.now(),
                                                comment = "创建时间")
    updated_at:Mapped[datetime] = mapped_column(DateTime,
                                                default=datetime.now(),
                                                comment = "更新时间")
    category_id:Mapped[int] = mapped_column(ForeignKey('category.id'),
                                            nullable = True,
                                            comment="博客分类ID")
    category:Mapped[Category] = relationship(back_populates="articles",
                                             lazy="joined")
    def __repr__(self):
        return (f"Article id={self.id},\ntitle={self.title},\n"
                f"content={self.content},\ncreated_at={self.created_at},\n"
                f"updated_at={self.updated_at}\n")





