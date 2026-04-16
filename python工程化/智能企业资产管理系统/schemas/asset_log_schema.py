from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class AssetLogBase(BaseModel):
    asset_id: int = Field(
        description="资产ID"
    )
    operate_user_id: int = Field(
        description="操作人ID"
    )
    operate_type: str = Field(
        description="操作类型（创建、更新、借用、归还等）",
        min_length=2,
        max_length=20
    )
    old_data: Optional[str | None] = Field(
        default=None,
        description="修改前数据",
        max_length=1000
    )
    new_data: Optional[str | None] = Field(
        default=None,
        description="修改后数据",
        max_length=1000
    )
    remark: Optional[str | None] = Field(
        default=None,
        description="备注",
        max_length=500
    )

    model_config = {
        "from_attributes": True,
        "json_schema_extra": {
            "example": {
                "asset_id": 1,
                "operate_user_id": 1,
                "operate_type": "借用",
                "old_data": "在用",
                "new_data": "借用",
                "remark": "员工张三借用"
            }
        }
    }

class AssetLogCreate(AssetLogBase):
    pass

class AssetLogOut(AssetLogBase):
    id: int = Field(description="日志ID")
    operate_time: datetime = Field(description="操作时间")