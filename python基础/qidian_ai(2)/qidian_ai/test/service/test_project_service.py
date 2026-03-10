import logging
from datetime import date

from schema.schema_module import ProjectModel
from service.project_service import ProjectService

logger = logging.getLogger(__name__)

def test_save():
    project: ProjectModel = ProjectModel(
        name="Stable Diffusion 3.0",
        star = 5,
        introduction = "Stable Diffusion是一款“稳定扩散”AI 图像生成器，可以免费创作出令人惊叹的图像。这是一款高质量的文本转图像模型，能够将您的想法转化为生动逼真的视觉效果。",
        link = "https://stabledifffusion.com/",
        added_on = date(2023, 6, 12),
        reviews = 10080,
        category_id = 2,
        detail = """<h2>从文本生成震撼图像</h2>
                    <p>释放您的想象力，并将其变为现实吧！使用我们的“文本转图像”功能，只需输入您的文本，我们的 AI 图像生成器就会将其转化为令人惊叹的图像，包括吉卜力工作室风格、宫崎骏、新海诚、小畑健等艺术家的风格以及更多。</p>
                    <h2>用 AI 精准度重塑图像</h2>
                    </p>借助我们强大的图像到图像的 AI 生成器，提升您的视觉效果。上传一张图片，并使用文本提示来引导转换——调整风格、改变场景、重新构想角色，或者生成具有惊人细节和真实感的惊人变体。基于稳定扩散技术，此工具非常适合概念艺术家、设计师和希望探索新风格或增强现有作品的创作者。</p>
                    <h2>使用稳定扩散进行智能图像编辑</h2>
                    <p>立即应用风格转换，将任何图像重新想象为水彩画、炭笔素描或充满活力的动漫插图。使用文本编辑功能，在图像中无缝修改标志、标签和横幅，同时保持其自然外观。进行精确的对象和场景调整，例如更改背景、添加天气效果或重新排列元素，同时保持图像的完整性。确保在多张图片中角色设计保持一致，保持服装、表情和情绪的稳定，以获得专业水准的成果。无论您是设计师、艺术家还是创作者，这款人工智能图像编辑工具都能提供无与伦比的创作控制力和基于直观文本提示的令人惊叹且逼真的效果。</p>
                """
    )

    service = ProjectService()
    service.save(project)

    logger.info(project)

    projects = service.get_by_category(2)
    logger.info("测试保存项目方法已完成，在分类[%s]中有项目记录数：%s",  2, len(projects))

    assert len(projects) > 0

def test_get():
    service = ProjectService()
    project = service.get(1)
    logger.info(project)