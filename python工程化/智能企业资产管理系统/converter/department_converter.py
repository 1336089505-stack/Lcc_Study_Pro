from models.department import Department
from schemas.department_schema import DepartmentBase

class DepartmentConverter:
    @staticmethod
    def department_to_model(department:Department) ->DepartmentBase:
        """
        Department 实体 → DepartmentBase
        :param department:
        :return:
        """
        return DepartmentBase.model_validate(department)

    @staticmethod
    def model_to_department(model:DepartmentBase) -> Department:
        """
        DepartmentBase → Department 实体
        :return:
        """
        data = model.model_dump(exclude_unset = True)
        return Department(**data)