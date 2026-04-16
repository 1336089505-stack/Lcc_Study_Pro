from models.asset import Asset
from schemas.asset_schema import AssetBase

class AssetConverter:
    @staticmethod
    def asset_to_model(asset:Asset) ->AssetBase:
        """
        Asset 实体 → AssetBase
        :param asset:
        :return:
        """
        return AssetBase.model_validate(asset)

    @staticmethod
    def model_to_asset(model:AssetBase) -> Asset:
        """
        AssetBase → Asset 实体
        :return:
        """
        data = model.model_dump(exclude_unset = True)
        return Asset(**data)