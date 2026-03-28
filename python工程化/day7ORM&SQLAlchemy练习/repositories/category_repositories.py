from sqlalchemy import select
from model import Article, Category
from sqlalchemy.orm import Session

class CategoryRepository():
    def __init__(self, session: Session):
        self.session = session

    def get_all(self,article: list[Category]):
        """
        添加文章
        :return:
        """
        self.session.add_all(article)