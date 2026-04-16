from sqlalchemy.orm import Session
from models.role import Role
from .base_repo import BaseRepository

class RoleRepository(BaseRepository[Role]):
    def __init__(self, session: Session):
        super().__init__(session, Role)