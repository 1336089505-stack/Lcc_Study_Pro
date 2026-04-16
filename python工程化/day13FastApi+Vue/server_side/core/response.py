from typing import TypeVar, Generic

from pydantic import BaseModel, Field

T = TypeVar("T")

class ApiResponse(BaseModel, Generic[T]):
    """
    API响应模型
    """
    code: int = Field(0, description="响应码")

    message: str = Field("", description="响应消息")

    data: T = Field(None, description="响应数据")

    model_config = {"from_attributes": True}

