
"""
设计一个博客系统，包含两个实体：博客文章（Article）和博客分类（Category）。要求如下：
•	使用SQLAlchemy 2.0的最新映射方式
•	文章实体包含：id（主键）、title（标题）、content（内容）、created_at（创建时间）、updated_at（更新时间）、category_id（外键）
•	分类实体包含：id（主键）、name（分类名称）、description（分类描述）、created_at（创建时间）
•	配置一对多关系：一个分类可以有多篇文章，一篇文章属于一个分类
•	使用级联操作：删除分类时，自动删除该分类下的所有文章
•	使用合适的lazy加载策略
•	编写代码实现以下功能：

"""
from session import get_session,engine
from repositories.article_repositories import ArticleRepository
from repositories.category_repositories import CategoryRepository
from model import Article, Category,Base

if __name__ == '__main__':
    """
    1.	创建数据库表
    """
    Base.metadata.create_all(engine)

    category_list = [
        Category(
            name = "娱乐类",
            description = "娱乐圈内八卦文章"
        ),
        Category(
            name="体育类",
            description="体育赛事等文章"
        ),
        Category(
            name="新闻类",
            description="国内国外重大新闻文章"
        )
    ]

    article_list = [
        # 娱乐类
        Article(
            title="某顶流明星被曝深夜聚餐，疑似新恋情曝光",
            content="据媒体爆料，近日某顶流男星被拍到与一位神秘女子深夜聚餐，两人举止亲密，结束后一同乘车离开，引发网友对其新恋情的猜测。",
            category=category_list[0]
        ),
        Article(
            title="热门综艺收视率再创新高，嘉宾互动成最大看点",
            content="本周播出的某热门户外综艺收视率突破3%，嘉宾们在任务中的趣味互动和真实反应，成为观众讨论的焦点，相关话题多次登上热搜。",
            category=category_list[0]
        ),
        Article(
            title="年度爆款电影票房破30亿，导演发文感谢观众",
            content="由知名导演执导的剧情片《XX》上映仅10天，票房便突破30亿大关，导演在社交媒体发文，感谢观众的支持与喜爱，并透露幕后拍摄故事。",
            category=category_list[0]
        ),
        # 体育类
        Article(
            title="国足世预赛关键战取胜，晋级希望重燃",
            content="在世界杯预选赛亚洲区比赛中，中国男足凭借下半场的两粒进球，2-0战胜对手，积分排名上升，为后续晋级保留了关键希望。",
            category=category_list[1]
        ),
        Article(
            title="NBA球星单场砍下60分，刷新个人生涯纪录",
            content="NBA常规赛中，某球星在对阵强敌的比赛中狂砍60分，同时贡献8篮板和5助攻，带领球队逆转取胜，也刷新了自己的单场得分纪录。",
            category=category_list[1]
        ),
        Article(
            title="网球名将斩获大满贯冠军，职业生涯第5次登顶",
            content="在法网男单决赛中，知名网球选手以3-1的比分战胜对手，成功夺得个人第5个大满贯冠军，重返世界排名第一的宝座。",
            category=category_list[1]
        ),
        # 新闻类
        Article(
            title="我国成功发射新一代气象卫星，监测能力大幅提升",
            content="今日，我国在文昌航天发射场成功发射新一代静止轨道气象卫星，该卫星将显著提升我国对极端天气的监测和预警能力，服务于防灾减灾工作。",
            category=category_list[2]
        ),
        Article(
            title="多国签署气候合作协议，承诺减少温室气体排放",
            content="在联合国气候变化大会上，超过50个国家共同签署新协议，承诺到2035年将温室气体排放量较2020年减少40%，推动全球绿色转型。",
            category=category_list[2]
        ),
        Article(
            title="国内多地出台稳就业政策，重点帮扶高校毕业生",
            content="为应对就业压力，北京、上海等多地发布稳就业新政，通过提供岗位补贴、创业扶持等措施，重点帮扶高校毕业生和困难群体实现就业。",
            category=category_list[2]
        )
    ]

    """
    2.	插入测试数据（至少2个分类，每个分类至少2篇文章）
    """
    # with get_session() as session:
    #     category_re = CategoryRepository(session)
    #     article_re = ArticleRepository(session)
    #
    #     category_re.get_all(category_list)
    #     article_re.get_all(article_list)

    """
    3.	根据文章ID查询文章及其所属分类信息（级联查询）
    """
    # with get_session() as session:
    #     article_re = ArticleRepository(session)
    #     ar_info = article_re.find_by_id_select_article_category(article_id=4)
    #     print(ar_info)

    """
    4.	查询所有分类及其包含的文章数量
    """
    # with get_session() as session:
    #     article_re = ArticleRepository(session)
    #     ar_info = article_re.find_all_category_and_articles_count()
    #     print(ar_info)
    """
    5.	查询特定分类下的所有文章
    """
    with get_session() as session:
        article_re = ArticleRepository(session)
        ar_info = article_re.find_by_category_select_all_article(2)
        print(ar_info)