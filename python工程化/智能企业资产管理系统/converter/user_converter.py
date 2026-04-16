from models.user import User
from schemas.user_schema import UserBase

class UserConverter:
    @staticmethod
    def user_to_model(user:User) ->UserBase:
        """
        User 实体 → UserBase
        :param user:
        :return:
        """
        return UserBase.model_validate(user)

    @staticmethod
    def model_to_user(model:UserBase) -> User:
        """
        UserBase → User 实体
        :return:
        """
        data = model.model_dump(exclude_unset = True)
        return User(**data)