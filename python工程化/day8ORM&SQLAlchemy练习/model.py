from datetime import datetime,date
from typing import Optional

from sqlalchemy import Integer, String, Float, DateTime, Numeric, Column, ForeignKey, Date, Enum, Table
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

movie_actor = Table(
    "movie_actor",
    Base.metadata,
    Column("movie_id", ForeignKey("movie.id"), primary_key=True),
    Column("actor_id", ForeignKey("actor.id"), primary_key=True),
)

class Category(Base):
    __tablename__ = 'category'
    id: Mapped[int] = mapped_column(Integer,
                                    primary_key=True,
                                    autoincrement=True,
                                    nullable=False,
                                    comment='电影分类ID')

    name: Mapped[str] = mapped_column(String(50),
                                      comment="分类名称")

    movies:Mapped[list["Movie"]] = relationship(back_populates="category",
                                                cascade = "all, delete-orphan",
                                                lazy="noload")
    def __repr__(self):
        return f"Category id={self.id},\nname={self.name},\n"



class Movie(Base):
    __tablename__ = 'movie'
    id: Mapped[int] = mapped_column(Integer,
                                    primary_key=True,
                                    autoincrement=True,
                                    nullable=False,
                                    comment='电影ID')

    title: Mapped[str] = mapped_column(String(50),
                                       comment="电影标题")
    mins:Mapped[int] = mapped_column(Integer,
                                     comment = "时长，单位为分钟")
    summary:Mapped[str] = mapped_column(String(500),
                                        comment = "介绍")
    release_date:Mapped[date] = mapped_column(Date,
                                              default=date.today(),
                                              comment = "发行时间")

    category_id: Mapped[int] = mapped_column(ForeignKey('category.id'),
                                             nullable=True,
                                             comment="电影分类ID")
    category: Mapped[Category] = relationship(back_populates="movies",
                                              lazy="joined")
    actors: Mapped[list["Actor"]] = relationship(
        secondary=movie_actor, back_populates="movies"
    )

    def __repr__(self):
        return (f"Movie id={self.id},\ntitle={self.title},\n"
                f"mins={self.mins},\nsummary={self.summary},\n"
                f"release_date={self.release_date},\n")


class Actor(Base):
    __tablename__ = 'actor'

    id: Mapped[int] = mapped_column(Integer,
                                    primary_key=True,
                                    autoincrement=True,
                                    nullable=False,
                                    comment='演员ID')
    name: Mapped[str] = mapped_column(String(50),
                                      comment="姓名")
    nickname: Mapped[str] = mapped_column(String(50),
                                          comment="昵称")
    gender:Mapped[str] = mapped_column(Enum('男','女'),
                                       comment = "性别")

    profile: Mapped[Optional["Profile"]] = relationship(
        back_populates="actor",
        uselist=False,
        cascade="all, delete-orphan",
        lazy="joined"
    )

    movies: Mapped[list["Movie"]] = relationship(
        secondary= movie_actor,
        back_populates="actors"
    )

    def __repr__(self):
        return (f"Category id={self.id},\nname={self.name},\n"
                f"nickname={self.nickname},\ngender={self.gender}\n")

class Profile(Base):
    __tablename__ = 'profile'
    id: Mapped[int] = mapped_column(ForeignKey('actor.id'),
                                    primary_key=True,
                                    comment='演员详情ID')

    constellation: Mapped[str] = mapped_column(String(50),
                                               comment="星座")
    blood_type: Mapped[str] = mapped_column(String(2),
                                            Enum('A','B','AB','O'),
                                            comment="血型")
    height: Mapped[int] = mapped_column(Integer,
                                        comment="身高，单位cm")
    weight: Mapped[int] = mapped_column(Integer,
                                        comment="体重，单位：kg")
    actor: Mapped[Actor] = relationship(
        back_populates="profile",
        lazy="joined")

    def __repr__(self):
        return (f"Profile id={self.id},\nconstellation={self.constellation},\n"
                f"blood_type={self.blood_type},\nheight={self.height},\n"
                f"weight={self.weight}\n")