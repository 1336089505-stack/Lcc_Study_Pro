import logging

from schema.schema_module import CategoryModel
from service.category_service import CategoryService

logger = logging.getLogger(__name__)

def test_get():
    service = CategoryService()
    category: CategoryModel = service.get(1)
    logger.info(category)
    assert  category is not None

def test_get():
    service = CategoryService()
    categories: list[CategoryModel] = service.get_all()
    for category in categories:
        logger.info(category)
    assert len(categories) > 0

def test_get_and_count_projects():
    service = CategoryService()
    categories: list[CategoryModel] = service.get_all_and_count_projects(None)
    for category in categories:
        logger.info(category)
    assert len(categories) > 0