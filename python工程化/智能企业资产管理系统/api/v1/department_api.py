from fastapi import APIRouter, Depends
from schemas.department_schema import DepartmentBase
from service.department_service import DepartmentService


router = APIRouter(prefix="/api/department", tags=["部门管理"])

# 依赖注入：每次请求创建新的 Service 实例
def get_department_service():
    return DepartmentService()

@router.get("/{dept_id}", summary="根据ID查询部门")
def get_department(
    dept_id: int,
    service: DepartmentService = Depends(get_department_service)
):
    data = service.get_by_id(dept_id)
    return data

@router.post("/add", summary="创建部门")
def add_department(
    dept: Department,
    service: DepartmentService = Depends(get_department_service)
):
    data = service.add(dept)


