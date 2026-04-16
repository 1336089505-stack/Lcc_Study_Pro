from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class News(Base):
    __tablename__ = 'news'

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    context = Column(String(255))
    datetime = Column(DateTime)
    author = Column(String(255))
    publish = Column(String(255))

    def __repr__(self):
        return (f"News id = {self.id},"
                f"title = {self.title},"
                f"context = {self.context},"
                f"datetime = {self.datetime},"
                f"author = {self.author}")