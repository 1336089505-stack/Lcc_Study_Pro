from pydantic import BaseModel, Field, FieldValidationInfo, field_validator
from typing import Optional
from datetime import date, datetime
from decimal import Decimal

class AssetBase(BaseModel):
    asset_code: str = Field(
        description="资产编码",
        min_length=5,
        max_length=30
    )
    name: str = Field(
        description="资产名称",
        min_length=2,
        max_length=100
    )
    category_id: int = Field(
        description="资产分类ID"
    )
    spec: Optional[str | None] = Field(
        default=None,
        description="资产规格",
        max_length=200
    )
    price: float = Field(
        description="资产单价",
        gt=0,
        max_digits=10,
        decimal_places=2
    )
    buy_time: date = Field(
        description="采购时间"
    )
    use_dept_id: Optional[int | None] = Field(
        default=None,
        description="使用部门ID"
    )
    use_user_id: Optional[int | None] = Field(
        default=None,
        description="使用人ID"
    )
    status: int = Field(
        description="状态（0 闲置，1 在用，2 维修，3 报废，4 借用）",
        ge=0,
        le=4
    )
    expire_time: Optional[date | None] = Field(
        default=None,
        description="报废/到期时间"
    )
    supplier: Optional[str | None] = Field(
        default=None,
        description="供应商",
        max_length=100
    )

    model_config = {
        "from_attributes": True,
        "json_schema_extra": {
            "example": {
                "asset_code": "ASSET-2024001",
                "name": "联想笔记本电脑",
                "category_id": 1,
                "spec": "i7, 16G, 512G",
                "price": 6999.99,
                "buy_time": "2024-01-01",
                "use_dept_id": 1,
                "use_user_id": 1,
                "status": 1,
                "expire_time": "2029-01-01",
                "supplier": "联想官方"
            }
        }
    }

class AssetCreate(AssetBase):
    pass

class AssetUpdate(AssetBase):
    pass

class AssetOut(AssetBase):
    id: int = Field(description="资产ID")
    create_date: datetime = Field(description="创建时间")
    update_date: datetime = Field(description="更新时间")

class AssetDetailOut(AssetOut):
    category_name: Optional[str | None] = Field(description="分类名称")
    use_dept_name: Optional[str | None] = Field(description="部门名称")
    use_user_name: Optional[str | None] = Field(description="使用人姓名")