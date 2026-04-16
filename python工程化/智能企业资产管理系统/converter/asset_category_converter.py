from models.asset_category import AssetCategory
from schemas.asset_category_schema import AssetCategoryBase

class AssetCategoryConverter:
    @staticmethod
    def asset_category_to_model(asset_category:AssetCategory) ->AssetCategoryBase:
        """
        AssetCategory 实体 → AssetCategoryBase
        :param asset_category:
        :return:
        """
        return AssetCategoryBase.model_validate(asset_category)

    @staticmethod
    def model_to_asset_category(model:AssetCategoryBase) -> AssetCategory:
        """
        AssetCategoryBase → AssetCategory 实体
        :return:
        """
        data = model.model_dump(exclude_unset = True)
        return AssetCategory(**data)