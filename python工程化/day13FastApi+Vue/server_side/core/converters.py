
from db.model import Book  # SQLAlchemy 实体类
from schema.schema_module import  BookModel  # Pydantic 模型

class BookConverter:
    def book_to_model(category: Book) -> BookModel:
        """Category 实体 → CategoryModel"""
        return BookModel.model_validate(category)

    def model_to_book(model: BookModel) -> Book:
        """CategoryModel → Category 实体"""
        data = model.model_dump(exclude_unset = True)
        return Book(**data)

