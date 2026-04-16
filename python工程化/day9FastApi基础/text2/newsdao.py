from sqlalchemy import create_engine,select
from sqlalchemy.orm import Session

from text2.news import News

engine = create_engine("mysql+pymysql://root:123456@localhost/day9_mysql")
session = None


def get_news():
    global session
    try:
        session = Session(engine)
        sets = select(News)

        result = result = session.execute(sets).scalars().all()
    finally:
        if session:
            session.close()
    return result

def get_by_id(news_id: int):
    global session
    try:
        session = Session(engine)
        sets = select(News).where(News.id == news_id)

        result = session.execute(sets).scalar_one_or_none()
    finally:
        if session:
            session.close()

    return result



