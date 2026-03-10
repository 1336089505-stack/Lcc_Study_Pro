from typing import Optional

from core.converters import CategoryConverter
from core.exceptions import QiDianAiException
from core.status_code import StatusCodes
from db.model import Category
from db.session import get_session
from repositories.category_repositories import CategoryRepository
from schema.schema_module import CategoryModel

class CategoryService:
    def __init__(self):
        pass

    def save(self, category: CategoryModel):
        """
        保存分类\n
        :param CategoryModel对象\n
        :return: 无
        """
        with get_session() as session:
            dao = CategoryRepository(session)
            entity = CategoryConverter.model_to_category(category) #model to orm
            dao.save(entity)

    def get(self, id: int) -> CategoryModel:
        """
        根据ID查询分类。 \n
        :param id: 分类ID \n
        :return: 返回CategoryModel
        """
        with get_session() as session:
            repository = CategoryRepository(session)
            category_entity: Category = repository.find_by_id(id)

            if not category_entity:
                raise QiDianAiException(StatusCodes.DATA_NOT_FOUND)

            category_model = CategoryConverter.category_to_model(category_entity)  # orm to model
            return  category_model

    def get_all(self) -> list[CategoryModel]:
        """
        查询所有分类

        :return: 返回分类列表，list[CategoryModel]
        """
        with get_session() as session:
            repository = CategoryRepository(session)
            categories = repository.find_all()
            return [CategoryConverter.category_to_model(category) for category in categories]

    def get_all_and_count_projects(self, id: Optional[int | None] = None):
        """
        查询所有分类，并统计分类下的项目数量\n
        :param id: 允许不传则查所有。如果指定ID则只查询该ID的分类和项目数量\n
        :return: list[CategoryModel]
        """
        with get_session() as session:
            repository = CategoryRepository(session)
            result = repository.find_and_count_projects(id)
            categories = []
            for category, project_count in result:
                category_model: CategoryModel = CategoryConverter.category_to_model(category)
                category_model.project_count = project_count
                categories.append(category_model)
        return categories