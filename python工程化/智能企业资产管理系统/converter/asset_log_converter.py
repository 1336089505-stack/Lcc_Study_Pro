from models.asset_log import AssetLog
from schemas.asset_log_schema import AssetLogBase

class AssetLogConverter:
    @staticmethod
    def asset_log_to_model(asset_log:AssetLog) ->AssetLogBase:
        """
        AssetLog 实体 → AssetLogBase
        :param asset_log:
        :return:
        """
        return AssetLogBase.model_validate(asset_log)

    @staticmethod
    def model_to_asset_log(model:AssetLogBase) -> AssetLog:
        """
        AssetLogBase → AssetLog 实体
        :return:
        """
        data = model.model_dump(exclude_unset = True)
        return AssetLog(**data)