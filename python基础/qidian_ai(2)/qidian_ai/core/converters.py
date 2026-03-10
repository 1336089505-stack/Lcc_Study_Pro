from datetime import date

from sqlalchemy.testing import exclude

from db.model import Project, Category  # SQLAlchemy 实体类
from schema.schema_module import ProjectModel, CategoryModel  # Pydantic 模型

class CategoryConverter:
    def category_to_model(category: Category) -> CategoryModel:
        """Category 实体 → CategoryModel"""
        return CategoryModel.model_validate(category)

    def model_to_category(model: CategoryModel) -> Category:
        """CategoryModel → Category 实体"""
        data = model.model_dump(exclude_unset = True)
        return Category(**data)

class ProjectConverter:
    def project_to_model(project: Project) -> ProjectModel:
        """Project 实体 → ProjectModel"""
        model_data = ProjectModel.model_validate(project).dict()  #, exclude("detail")
        # 如果有关系字段，也可以额外设置 category_id
        if project.category:
            model_data["category"] = project.category
        return ProjectModel(**model_data)

    def model_to_project(model: ProjectModel) -> Project:
        """ProjectModel → Project 实体"""
        data = model.model_dump(exclude_unset=True)
        # 可以单独处理 datetime / date 类型
        if "added_on" not in data or data["added_on"] is None:
            data["added_on"] = date.today()
        return Project(**data)