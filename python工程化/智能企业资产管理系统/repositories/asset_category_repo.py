from sqlalchemy.orm import Session
from models.asset_category import AssetCategory
from .base_repo import BaseRepository

class AssetCategoryRepository(BaseRepository[AssetCategory]):
    def __init__(self, session: Session):
        super().__init__(session, AssetCategory)