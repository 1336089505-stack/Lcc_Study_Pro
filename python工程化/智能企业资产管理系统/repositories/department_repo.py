from sqlalchemy.orm import Session
from models.department import Department
from .base_repo import BaseRepository

class DepartmentRepository(BaseRepository[Department]):
    def __init__(self, session: Session):
        super().__init__(session, Department)