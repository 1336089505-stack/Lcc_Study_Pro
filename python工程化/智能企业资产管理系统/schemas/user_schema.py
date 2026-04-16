from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    username: str = Field(
        description="登录账号",
        min_length=3,
        max_length=50
    )
    name: str = Field(
        description="真实姓名",
        min_length=2,
        max_length=20
    )
    phone: Optional[str | None] = Field(
        default=None,
        description="手机号",
        min_length=11,
        max_length=11
    )
    dept_id: Optional[int | None] = Field(
        default=None,
        description="所属部门ID"
    )
    role_id: Optional[int | None] = Field(
        default=None,
        description="所属角色ID"
    )
    status: Optional[int | None] = Field(
        default=1,
        description="状态（0 禁用，1 正常）"
    )

    model_config = {
        "from_attributes": True,
        "json_schema_extra": {
            "example": {
                "username": "admin",
                "name": "张三",
                "phone": "13800138000",
                "dept_id": 1,
                "role_id": 1,
                "status": 1
            }
        }
    }

class UserCreate(UserBase):
    password: str = Field(
        description="密码",
        min_length=6,
        max_length=255
    )

class UserUpdate(UserBase):
    password: Optional[str | None] = Field(
        default=None,
        description="新密码（不填则不改）",
        min_length=6
    )

class UserOut(UserBase):
    id: int = Field(description="用户ID")
    last_login: Optional[datetime | None] = Field(description="最后登录时间")
    create_time: datetime = Field(description="创建时间")

class UserDetailOut(UserOut):
    role_name: Optional[str | None] = Field(description="角色名称")
    dept_name: Optional[str | None] = Field(description="部门名称")