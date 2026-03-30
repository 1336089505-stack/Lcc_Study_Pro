from sqlalchemy import select
from model import Category,Movie,Actor,Profile
from sqlalchemy.orm import Session

class CategoryRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self,category: list[Category]):
        """
        添加文章
        :return:
        """
        self.session.add_all(category)

    """
    4. 	根据主键查询电影信息（包括对应的分类）
    """
    def find_by_id_movie(self,movie_id: int):
        stat = (select(Movie, Category).where(Movie.id == movie_id)
                .join(Category, Category.id == Movie.category_id))

        result = self.session.execute(stat).all()
        return result

    """
    5. 	查询所有的电影（包括对应的分类）
    """
    def find_all_movie_and_category(self):
        stat = (select(Movie, Category.name)
                .join(Category, Category.id == Movie.category_id))
        result = self.session.execute(stat).all()
        return result

    """
    6. 	根据主键查询演员信息（包括演员详细资料）
    """
    def find_by_id_select_actory_and_profile(self,actor_id: int):
        stat = select(Actor,Profile).join(Actor.profile).where(Actor.id == actor_id)

        result = self.session.execute(stat).all()
        return result

    """
    7. 	查询某个电影及其所有的主演
    """
    def find_by_movie_select_all_movie_actor(self,movie_id: int):
        stmt = (
            select(Movie, Actor)
            .join(Movie.actors)  # 建立电影和演员的关联
            .where(Movie.id == movie_id)
        )
        result = self.session.execute(stmt).all()
        return result

    """
    8. 	查询某个演员演过哪些电影
    """
    def get_actor_movies(self, actor_id: int):
        stmt = (
            select(Actor, Movie)
            .join(Actor.movies)  # 建立演员和电影的关联
            .where(Actor.id == actor_id)
        )
        result = self.session.execute(stmt).all()
        return result

