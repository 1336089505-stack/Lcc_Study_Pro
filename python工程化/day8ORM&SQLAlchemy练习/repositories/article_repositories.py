from sqlalchemy import select, func
from model import Article, Category
from sqlalchemy.orm import Session

class ArticleRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self,article: list[Article]):
        """
        添加文章
        :return:
        """
        self.session.add_all(article)
    """
    3.	根据文章ID查询文章及其所属分类信息（级联查询）
    """
    def find_by_id_select_article_category(self,article_id: int):
        stat = (select(Article,Category).where(Article.id == article_id)
                .join(Category, Category.id == Article.category_id))
        result = self.session.execute(stat).all()
        return result

    """
    4.	查询所有分类及其包含的文章数量
    """
    def find_all_category_and_articles_count(self):
        stat = (select(Category,func.count(Article.category_id))
                .join(Category, Category.id == Article.category_id)
                .group_by(Category.id))
        result = self.session.execute(stat).all()
        return result

    """
    5.	查询特定分类下的所有文章
    """
    def find_by_category_select_all_article(self,category_id: int):
        stat = (select(Category.name,Article.title)
                .join(Category, Category.id == Article.category_id)
                .where(Category.id == category_id))
        result = self.session.execute(stat).all()
        return result



