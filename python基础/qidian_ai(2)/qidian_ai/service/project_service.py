from core.exceptions import QiDianAiException
from core.status_code import StatusCodes
from db.model import Project
from db.session import get_session
from repositories.project_repositories import ProjectRepository
from schema.schema_module import ProjectModel
from core.converters import ProjectConverter

class ProjectService:
    def __init__(self):
        pass

    def save(self,  project: ProjectModel):
        """
        保存项目\n
        :param: ProjectModel对象
        :return: 无
        """
        with get_session() as session:
            repository = ProjectRepository(session)
            project_entity = ProjectConverter.model_to_project(project)
            repository.save(project_entity)

    def get(self, id: int) -> ProjectModel:
        """
        根据ID查询项目 \n
        :param id: 必填 \n
        :return: ProjectModel对象，或None
        """
        with get_session() as session:
            repository = ProjectRepository(session)
            project_entity: Project = repository.find_by_id(id)

            if not project_entity:
                raise QiDianAiException(StatusCodes.DATA_NOT_FOUND)

            return ProjectConverter.project_to_model(project_entity)

    def get_by_category(self, category_id: int) -> list[ProjectModel]:
        """
        根据分类查询项目\n
        :param category_id:分类ID\n
        :return: list[ProjectModel]
        """
        with get_session() as session:
            repository = ProjectRepository(session)
            projects = repository.find_by_category(category_id)
            return [ProjectConverter.project_to_model(project) for project in projects]