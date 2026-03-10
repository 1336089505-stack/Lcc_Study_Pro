from sqlalchemy import select
from sqlalchemy.orm import Session

from db.model import Project


class ProjectRepository:

    def __init__(self, session: Session):
        self.session = session

    def save(self, project: Project):
        """
        保存项目
        :param project:
        :return:
        """
        self.session.add(project)
        self.session.flush()
        print(self.session)

    def find_by_id(self, id: int):
        """
        根据ID查询
        :param id:
        :return:
        """
        statement = select(Project).where(Project.id == id)
        result = self.session.execute(statement)
        project = result.scalars().one_or_none()
        return project

    def find_by_category(self, category_id: int):
        statement = select(Project).where(Project.category_id == category_id)
        result = self.session.execute(statement)
        projects = result.scalars().all()
        return projects
