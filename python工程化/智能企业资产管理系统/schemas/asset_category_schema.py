from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class AssetCategoryBase(BaseModel):
    name: str = Field(
        description="分类名称",
        min_length=2,
        max_length=50
    )
    code: str = Field(
        description="分类编码",
        min_length=2,
        max_length=30
    )
    parent_id: Optional[int | None] = Field(
        default=None,
        description="上级分类ID"
    )
    desc: Optional[str | None] = Field(
        default=None,
        description="分类描述",
        max_length=200
    )

    model_config = {
        "from_attributes": True,
        "json_schema_extra": {
            "example": {
                "name": "办公设备",
                "code": "OFFICE",
                "parent_id": None,
                "desc": "打印机、电脑等"
            }
        }
    }

class AssetCategoryCreate(AssetCategoryBase):
    pass

class AssetCategoryUpdate(AssetCategoryBase):
    pass

class AssetCategoryOut(AssetCategoryBase):
    id: int = Field(description="分类ID")
    create_time: datetime = Field(description="创建时间")

class AssetCategoryTreeOut(AssetCategoryOut):
    children: List["AssetCategoryTreeOut"] = Field(
        default=[],
        description="子分类列表"
    )

AssetCategoryTreeOut.model_rebuild()