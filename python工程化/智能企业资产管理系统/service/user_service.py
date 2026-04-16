from models.user import User
from core.database import get_session
from repositories.user_repo import UserRepository
from converter.user_converter import UserConverter
from schemas.user_schema import UserBase


class UserService:
    def __init__(self):
        pass

    def add(self, user: User):
        """
        添加
        :param user:
        :return:
        """
        with get_session() as session:
            repo = UserRepository(session)
            entity = UserConverter.model_to_user(user)
            repo.add(entity)

    def get_by_id(self, dept_id: int) -> UserBase:
        with get_session() as session:
            repo = UserRepository(session)
            entity = repo.get_by_id(dept_id)
            # 实体转模型返回
            return UserConverter.user_to_model(entity)