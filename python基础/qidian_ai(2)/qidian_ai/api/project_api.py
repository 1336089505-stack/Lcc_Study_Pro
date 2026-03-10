from typing import Annotated

from fastapi import APIRouter, Query, Path

from core.qidian_response import success, ApiResponse
from schema.schema_module import ProjectModel
from service.project_service import ProjectService

router = APIRouter(tags = ["项目模块"])  #description = "项目模块接口"

@router.get("/get/{id}", response_model = ApiResponse, description="获取指定项目详情")
def get(id: Annotated[int, Path(description="项目ID", gt = 0)]):
    service = ProjectService()
    project = service.get(id)
    return  success(project) #->ApiResponse


@router.get("/list/c{category_id}", description="获取某分类下详情列表", response_model = ApiResponse)
def get_project_list(category_id: Annotated[int, Path(description="分类ID", gt = 0)]):
    """
    获取项目列表\n
    请求方式：http://localhost/app/v1/project/list/c1
    :param category_id:
    :return:
    """
    service = ProjectService()
    projects = service.get_by_category(category_id)
    return success(projects)