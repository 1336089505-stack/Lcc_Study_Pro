from pydantic import BaseModel

class QuestionModel(BaseModel):
    id: int | None = None
    title: str
    content: str
    answer:str
    level:str
    type:str
    tags:str
    score:int

    model_config = {
        "from_attributes": True  # <- Pydantic v2 替代 orm_mode=True,允许 from_orm 使用 SQLAlchemy 对象 """
    }
