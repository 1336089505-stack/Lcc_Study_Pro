`from datetime import date
from typing import Optional

from pydantic import BaseModel, Field

class CategoryModel(BaseModel):
    name: str      = Field(
        description="项目分类名称",
        min_length = 2,
        max_length = 32
    )

    emoji: Optional[ str | None ]     = Field(
        default = None,
        description="项目分类图标",
        min_length = 1,
        max_length = 32
    )

    project_count: Optional[ int | None ] = Field(
        default = None,
        description = "项目数量"
    )

    model_config = {
        "from_attributes": True  # <- Pydantic v2 替代 orm_mode=True,允许 from_orm 使用 SQLAlchemy 对象 """
    }


class ProjectModel(BaseModel):

    name: str = Field(
        description="项目名称",
        min_length = 2,
        max_length = 128,
        json_schema_extra={
            "error_message":{
                "required":"项目名称必须填写"
            }
        }
    )

    star: Optional[ int | None ]  = Field(
        description = "项目标星",
        gt = 0
    )

    introduction: str = Field(
        description = "项目介绍",
        max_length = 500
    )

    added_on: Optional[ date | None ] = Field(
        default = date.today,
        description = "收录时间"
    )

    reviews: Optional[ int | None ] = Field(
        default = None,
        description = "项目浏览量"
    )

    link: Optional[ str | None ] = Field(
        default = None,
        description = "项目链接",
        max_length = 128
    )

    category_id: Optional[int | None] = Field(
        default = None,
        description="分类"
    )

    detail: Optional[ str | None ] = Field(
        default = None,
        description = "项目详情"
    )

    model_config = {
        "from_attributes": True
    }