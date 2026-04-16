from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class RoleBase(BaseModel):
    name: str = Field(
        description="角色名称",
        min_length=2,
        max_length=30
    )
    desc: Optional[str | None] = Field(
        default=None,
        description="角色描述",
        max_length=200
    )
    menu_ids: Optional[str | None] = Field(
        default="",
        description="关联菜单ID字符串（逗号分隔）",
        max_length=500
    )
    status: Optional[int | None] = Field(
        default=1,
        description="状态（0 禁用，1 正常）"
    )

    model_config = {
        "from_attributes": True,
        "json_schema_extra": {
            "example": {
                "name": "管理员",
                "desc": "系统管理员",
                "menu_ids": "1,2,3",
                "status": 1
            }
        }
    }

class RoleCreate(RoleBase):
    pass

class RoleUpdate(RoleBase):
    pass

class RoleOut(RoleBase):
    id: int = Field(description="角色ID")
    create_time: datetime = Field(description="创建时间")