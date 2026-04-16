from datetime import date
from typing import Optional, List

from pydantic import BaseModel, Field

class BookModel(BaseModel):
    id: int = Field(
        default=None,
        description="书籍id"
    )
    name: str      = Field(
        description="书籍名称",
        min_length = 1,
        max_length = 32
    )
    category: str  = Field(
        description="书籍分类",
        min_length = 1,
        max_length = 32
    )

    binding: str = Field(
        description="书籍装帧",
        min_length=1,
        max_length=32
    )

    tags: List[str] = Field(
        description="书籍标签",
        min_length=1,
        max_length=200
    )

    price: float = Field(
        description="书籍价格",
        gt=0
    )
    is_sale: bool = Field(
        description="是否在售",
    )
    model_config = {
        "from_attributes": True  # <- Pydantic v2 替代 orm_mode=True,允许 from_orm 使用 SQLAlchemy 对象 """
    }

class BookRequest(BaseModel):
    id: int