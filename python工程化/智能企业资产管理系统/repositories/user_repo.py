from sqlalchemy.orm import Session
from models.user import User
from .base_repo import BaseRepository

class UserRepository(BaseRepository[User]):
    def __init__(self, session: Session):
        super().__init__(session, User)