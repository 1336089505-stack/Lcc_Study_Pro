"""
题目：设计一个电影管理系统
实体类
设计一个简单的电影管理系统，包含以下实体：
1. 	分类（Category）：包含id（主键）、name（名称）
2. 	电影（Movie）：包含id（主键）、title（电影标题）、mins（时长，单位为分钟）、
summary（介绍，长度500字）、release_date（发行时间）
3. 	演员（Actor）：包含id（主键）、name（姓名）、nickname（昵称）、gender（性别）
4. 	演员详情（Profile）：包含id（主键）、constellation（星座）、blood_type（血型）、height（身高，单位cm）、weight（体重，单位：kg）
5. 	主演（MovieActor）：包含movie_id（主键1，关联电影）、actor_id（主键2，关联演员）
关系说明：
1、多对一关系：电影与分类，一个分类有多个电影，一个电影属于一个分类
2、一对一关系：演员与演员详细信息，
3、多对多关系：电影与演员，构成主演记录
要求：
使用SQLAlchemy 2.0的最新映射方式（DeclarativeBase、Mapped、mapped_column等）
配置所有上述关系，并设置合适的级联操作和lazy加载策略
编写完整的Python代码，包括：
1. 	模型定义
2. 	数据库连接和表创建
3. 	插入测试数据
4. 	根据主键查询电影信息（包括对应的分类）
5. 	查询所有的电影（包括对应的分类）
6. 	根据主键查询演员信息（包括演员详细资料）
7. 	查询某个电影及其所有的主演
8. 	查询某个演员演过哪些电影
"""
from datetime import datetime,date
from typing import Optional

from sqlalchemy import Integer, String, Float, DateTime, Numeric, Column, ForeignKey, Date, Enum
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


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
        pass

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

    def __repr__(self):
        pass

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
    gender:Mapped[str] = mapped_column(String(50),
                                       Enum('男','女'),
                                       comment = "性别")

    profile: Mapped[Optional["Profile"]] = relationship(
        back_populates="profile",
        uselist=False,  # 一对一关系的关键！
        cascade="all, delete-orphan",  # 级联删除
        lazy="joined"  # 立即加载
    )

    # 关系：多对多 → 电影
    movies: Mapped[list["Movie"]] = relationship(
        secondary="movie_actor",
        back_populates="actors"
    )

    def __repr__(self):
        pass

class Profile(Base):
    __tablename__ = 'profile'
    id: Mapped[int] = mapped_column(Integer,
                                    primary_key=True,
                                    autoincrement=True,
                                    nullable=False,
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
        back_populates="actor",
        lazy="joined")

    def __repr__(self):
        pass


class MovieActor(Base):
    __tablename__ = 'movie_actor'

    movie_id: Mapped[int] = mapped_column(Integer,
                                    ForeignKey("movie.id", ondelete="CASCADE"),
                                    autoincrement=True,
                                    nullable=False,
                                    comment='演员详情ID')
    actor_id: Mapped[int] = mapped_column(Integer,
                                    primary_key=True,
                                    autoincrement=True,
                                    nullable=False,
                                    comment='演员详情ID')

    def __repr__(self):
        pass








