from typing import TypeVar, Generic

from pydantic import BaseModel, Field

from core.status_code import StatusCodes

T = TypeVar("T")

class ApiResponse(BaseModel, Generic[T]):
    """
    API响应模型
    """
    code: int = Field(0, description="响应码")

    message: str = Field("", description="响应消息")

    data: T = Field(None, description="响应数据")

    model_config = {"from_attributes": True}

def success(data: T = None) -> ApiResponse[T]:
    status_code = StatusCodes.SUCCESS
    return ApiResponse(code = status_code.code, message = status_code.message, data = data)

def fail(status_code: StatusCodes, message: str = None, data: T = None) -> ApiResponse[None]:
    return ApiResponse(code = status_code.code, message = (message or status_code.message), data = data)