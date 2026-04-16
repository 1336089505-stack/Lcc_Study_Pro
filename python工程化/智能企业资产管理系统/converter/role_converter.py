from models.role import Role
from schemas.role_schema import RoleBase

class RoleConverter:
    @staticmethod
    def role_to_model(role:Role) ->RoleBase:
        """
        role 实体 → RoleBase
        :param role:
        :return:
        """
        return RoleBase.model_validate(role)

    @staticmethod
    def model_to_role(model:RoleBase) -> Role:
        """
        RoleBase → Role 实体
        :return:
        """
        data = model.model_dump(exclude_unset = True)
        return Role(**data)