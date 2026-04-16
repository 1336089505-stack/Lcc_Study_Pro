from models.department import Department
from core.database import get_session
from repositories.department_repo import DepartmentRepository
from converter.department_converter import DepartmentConverter
from schemas.department_schema import DepartmentBase


class DepartmentService:
    def __init__(self):
        pass

    def add(self, department: Department):
        """
        添加
        :param department:
        :return:
        """
        with get_session() as session:
            repo = DepartmentRepository(session)
            entity = DepartmentConverter.model_to_department(department)
            repo.add(entity)

    def get_by_id(self, dept_id: int) -> DepartmentBase:
        with get_session() as session:
            repo = DepartmentRepository(session)
            entity = repo.get_by_id(dept_id)
            # 实体转模型返回
            return DepartmentConverter.department_to_model(entity)