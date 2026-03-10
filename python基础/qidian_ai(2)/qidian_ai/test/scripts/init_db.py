import logging

from unicodedata import category

from db.model import Base
from db.session import engine
from schema.schema_module import CategoryModel
from service.category_service import CategoryService

logger = logging.getLogger(__name__)

def test_init_db():

    logger.info("开始初始化数据库......")
    Base.metadata.create_all(engine)

    categories = [
        CategoryModel(name='写作与编辑', emoji='✍️'),
        CategoryModel(name='图像生成与编辑', emoji='🖼️'),
        CategoryModel(name='图像分析', emoji='🔍️'),
        CategoryModel(name='音乐与音频', emoji="🎵"),
        CategoryModel(name='语音生成与转换', emoji='🎤'),
        CategoryModel(name='艺术与创意设计', emoji='🎨'),
        CategoryModel(name='社交媒体', emoji='💬'),
        CategoryModel(name='AI检测与反检测', emoji='🛡️'),
        CategoryModel(name='编程与开发', emoji='💻'),
        CategoryModel(name='视频与动画', emoji='🎬'),
        CategoryModel(name='日常生活', emoji='🏠'),
        CategoryModel(name='法律与金融', emoji='⚖️'),
        CategoryModel(name='商业管理', emoji='📊'),
        CategoryModel(name='市场营销与广告', emoji='📢'),
        CategoryModel(name='健康与养生', emoji='❤️'),
        CategoryModel(name='商业研究', emoji='📈'),
        CategoryModel(name='教育与翻译', emoji='🌐'),
        CategoryModel(name='聊天机器人与虚拟伴侣', emoji='🎭'),
        CategoryModel(name='室内与建筑设计', emoji='🏛️'),
        CategoryModel(name='办公与效率提升', emoji='📋'),
        CategoryModel(name='研究与数据分析', emoji='📚'),
        CategoryModel(name='其他', emoji='🎲')
    ]

    category_service = CategoryService()

    cs = category_service.get_all();
    len_ = len(cs)
    if len_ > 0:
        logger.info(f"数据库已存在{len_}条分类，请勿重复初始化")
    else:
        for category in categories:
            category_service.save( category)
        logger.info(f"已初始化{len(categories)}条分类。")