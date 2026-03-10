import logging
from typing import Annotated

from fastapi import APIRouter, Query

from core.qidian_response import success, ApiResponse
from schema.schema_module import CategoryModel
from service.category_service import CategoryService

logger = logging.getLogger(__name__)

router = APIRouter(tags = ["分类模块"]) #description = "分类模块接口",

@router.get("/get/{id}", response_model = ApiResponse, description="获取指定分类详情")
def get_category(id: int) -> ApiResponse[CategoryModel]:
    """
    获取分类\n
    :param id:
    :return:
    """
    logger.debug("is: %s", id)
    service = CategoryService()
    category = service.get(id)

    return success(category)

@router.get("/list", description="获取所有分类", response_model = ApiResponse)
def get_categories(iscount: Annotated[bool, Query(description="是否同步返回项目数量")] = None):
    """
    获取所有分类，如果需要统计数量 \n
    :param: iscount 是否统计项目数据\n
    :return:
    """
    categories = None

    service = CategoryService()

    logger.info("iscount: %s", iscount)

    if iscount:
        categories = service.get_all_and_count_projects()
    else:
        categories = service.get_all()


    return success(categories)