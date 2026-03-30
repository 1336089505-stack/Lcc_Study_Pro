from sqlalchemy import select
from model import Profile
from sqlalchemy.orm import Session

class ProfileRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self,profile: list[Profile]):
        """
        添加文章
        :return:
        """
        self.session.add_all(profile)