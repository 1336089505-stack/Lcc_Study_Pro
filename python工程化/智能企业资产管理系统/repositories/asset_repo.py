from sqlalchemy.orm import Session
from models.asset import Asset
from .base_repo import BaseRepository

class AssetRepository(BaseRepository[Asset]):
    def __init__(self, session: Session):
        super().__init__(session, Asset)