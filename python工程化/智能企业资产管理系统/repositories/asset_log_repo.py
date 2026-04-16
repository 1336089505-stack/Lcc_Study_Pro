from sqlalchemy.orm import Session
from models.asset_log import AssetLog
from .base_repo import BaseRepository

class AssetLogRepository(BaseRepository[AssetLog]):
    def __init__(self, session: Session):
        super().__init__(session, AssetLog)