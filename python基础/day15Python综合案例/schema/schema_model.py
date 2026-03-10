from pydantic import BaseModel,Field
#数据模型，与数据库接口交互
class CustomerModel(BaseModel):
    #Field添加额外的校验规则
    name: str = Field(
        #接口文档显示描述
        description="The name of the customer",
        min_length=1,
        max_length=30,
    )
    age: int = Field(
        description="The age of the customer",
        default=None
    )
    phone: str = Field(
        description="The phone number of the customer",
        default=None,
        min_length=0,
        max_length=20
    )
    email: str = Field(
        description="The email of the customer",
        default=None,
        min_length=0,
        max_length=30
    )