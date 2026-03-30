from sqlalchemy import select
from model import Actor
from sqlalchemy.orm import Session

class ActorRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self,actor: list[Actor]):
        """
        添加文章
        :return:
        """
        self.session.add_all(actor)