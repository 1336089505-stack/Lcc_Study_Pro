from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class DepartmentBase(BaseModel):
    name: str = Field(
        description="部门名称",
        min_length=2,
        max_length=50
    )
    parent_id: Optional[int | None] = Field(
        default=None,
        description="上级部门ID（顶级为 null）"
    )
    status: Optional[int | None] = Field(
        default=1,
        description="状态（0 禁用，1 正常）"
    )

    model_config = {
        "from_attributes": True,
        "json_schema_extra": {
            "example": {
                "name": "技术部",
                "parent_id": 1,
                "status": 1
            }
        }
    }

class DepartmentCreate(DepartmentBase):
    pass

class DepartmentUpdate(DepartmentBase):
    pass

class DepartmentOut(DepartmentBase):
    id: int = Field(description="部门ID")
    create_time: datetime = Field(description="创建时间")

class DepartmentTreeOut(DepartmentOut):
    children: List["DepartmentTreeOut"] = Field(
        default=[],
        description="子部门列表"
    )

# 解决递归引用
DepartmentTreeOut.model_rebuild()