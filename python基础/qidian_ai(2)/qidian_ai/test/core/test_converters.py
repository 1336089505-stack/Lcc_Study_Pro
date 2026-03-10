from core.converters import CategoryConverter
from db.model import Category
from schema.schema_module import CategoryModel


def test_category_to_model():
    category: Category = Category(id=1, name="测试分类1", emoji="0x87f98a")
    model: CategoryModel = CategoryConverter.category_to_model(category)
    print( model)

def test_model_to_category():
    model: CategoryModel = CategoryModel(name="测试分类2", emoji="0x87f98a")
    category: Category = CategoryConverter.model_to_category(model)
    print( category)