from typing import Generic, TypeVar, Type, List, Optional, Dict, Any
from sqlalchemy.orm import Session
from sqlalchemy import select, func

from core.database import Base

ModelType = TypeVar("ModelType", bound=Base)

class BaseRepository(Generic[ModelType]):
    def __init__(self, session: Session, model: Type[ModelType]):
        """
        初始化
        :param session:
        :param model:
        """
        self.session = session
        self.model = model

    def get_by_id(self, id: int) -> Optional[ModelType]:
        """
        根据ID查询
        :param id:
        :return:
        """
        return self.session.get(self.model, id)

    def get_all(self) -> List[ModelType]:
        """
        查询所有
        :return:
        """
        stmt = select(self.model)
        return list(self.session.scalars(stmt).all())


    def add(self, entity: ModelType) -> None:
        """
        添加
        :param entity:
        :return:
        """
        self.session.add(entity)

    def delete(self, id: int) -> bool:
        """
        删除
        :param id:
        :return:
        """
        obj = self.get_by_id(id)
        if not obj:
            return False
        self.session.delete(obj)
        return True

    def count(self) -> int:
        """
        统计数量
        :return:
        """
        stmt = select(func.count()).select_from(self.model)
        return self.session.scalar(stmt) or 0