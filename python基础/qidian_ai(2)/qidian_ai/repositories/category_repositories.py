from typing import Optional

from sqlalchemy import select, func
from sqlalchemy.orm import Session

from db.model import Category, Project


class CategoryRepository:

    def __init__(self, session: Session):
        self.session = session
        pass

    def save(self, category: Category):
        self.session.add(category)

    def find_by_id(self, id: int) -> Category:
        return self.session.get(Category, id)

    def find_all(self) -> list[Category]:
        statement = select(Category)
        result = self.session.scalars(statement)
        categories = result.all()
        return categories

    def find_and_count_projects(self, id: Optional[int | None]):
        stmt = (
            select(
                Category,
                func.count(Project.id).label("project_count")
            )
            .outerjoin(Project, Category.projects)
            .group_by(Category.id)
            .order_by(Category.id)
            #.order_by(func.count(Project.id).desc())
        )
        if id:
            stmt = stmt.where(Category.id == id)

        results = self.session.execute(stmt).all()
        """
        print( results)

        print("\n🏆 分类项目数量排名")
        print("=" * 60)
        print(f"{'排名':<4} {'分类':<12} {'图标':<4} {'项目数':<8} {'占比':<8}")
        print("-" * 60)

        for category, project_count,  in results:
            print(category)
            print(project_count)
        """

        return  results