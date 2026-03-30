from sqlalchemy import select
from model import Movie
from sqlalchemy.orm import Session

class MovieRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self,movie: list[Movie]):
        """
        添加文章
        :return:
        """
        self.session.add_all(movie)