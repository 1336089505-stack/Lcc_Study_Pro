from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Question(Base):
    __tablename__ = 'question'
    id = Column(Integer, primary_key=True,autoincrement=True)
    title = Column(String(255))
    content = Column(String(255))
    answer = Column(String(255))
    level = Column(String(255))
    type = Column(String(255))
    tags = Column(String(255))
    score = Column(Integer)

    def __repr__(self):
        return (f"Question id={self.id},\ntitle={self.title},\n"
                f"content={self.content},\nanswer={self.answer},\n"
                f"level={self.level},\ntype={self.type},\ntags={self.tags},\n"
                f"score={self.score}")

