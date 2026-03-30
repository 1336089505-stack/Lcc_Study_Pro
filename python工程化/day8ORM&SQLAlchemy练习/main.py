from datetime import date

from session import get_session,engine
from model import Category,Movie,Actor,Profile,Base
from repositories.actor_repositories import ActorRepository
from repositories.movie_repositories import MovieRepository
from repositories.profile_repositories import ProfileRepository
from repositories.category_repositories import CategoryRepository
"""
题目：设计一个电影管理系统
实体类
设计一个简单的电影管理系统，包含以下实体：
1. 	分类（Category）：包含id（主键）、name（名称）
2. 	电影（Movie）：包含id（主键）、title（电影标题）、mins（时长，单位为分钟）、
summary（介绍，长度500字）、release_date（发行时间）
3. 	演员（Actor）：包含id（主键）、name（姓名）、nickname（昵称）、gender（性别）
4. 	演员详情（Profile）：包含id（主键）、constellation（星座）、blood_type（血型）、height（身高，单位cm）、weight（体重，单位：kg）
5. 	主演（MovieActor）：包含movie_id（主键1，关联电影）、actor_id（主键2，关联演员）
关系说明：
1、多对一关系：电影与分类，一个分类有多个电影，一个电影属于一个分类
2、一对一关系：演员与演员详细信息，
3、多对多关系：电影与演员，构成主演记录
要求：
使用SQLAlchemy 2.0的最新映射方式（DeclarativeBase、Mapped、mapped_column等）
配置所有上述关系，并设置合适的级联操作和lazy加载策略
编写完整的Python代码，包括：
6. 	根据主键查询演员信息（包括演员详细资料）
7. 	查询某个电影及其所有的主演
8. 	查询某个演员演过哪些电影
"""

if __name__ == '__main__':
    """
    1.	创建数据库表
    """
    Base.metadata.create_all(engine)

    """
    3. 	插入测试数据
    """
    # 1. 分类
    cate1 = Category(name="科幻")
    cate2 = Category(name="动作")
    cate3 = Category(name="喜剧")


    # 2. 电影
    movie1 = Movie(
        title="星际穿越",
        mins=169,
        summary="一组探险家利用虫洞穿越星际，寻找人类新家园。",
        release_date=date(2014, 11, 7),
        category_id=1
    )
    movie2 = Movie(
        title="速度与激情",
        mins=106,
        summary="街头赛车手与警方的较量，充满刺激的飞车追逐。",
        release_date=date(2001, 6, 22),
        category_id=2
    )
    movie3 = Movie(
        title="人在囧途",
        mins=95,
        summary="春运路上的搞笑奇遇，充满温情与爆笑。",
        release_date=date(2010, 6, 4),
        category_id=3
    )

    # 3. 演员 + 详情
    # 演员1
    a1 = Actor(name="马修·麦康纳", nickname="马修", gender="男")
    a1.profile = Profile(
        constellation="天蝎座",
        blood_type="A",
        height=182.0,
        weight=78.0
    )
    # 演员2
    a2 = Actor(name="范·迪塞尔", nickname="范叔", gender="男")
    a2.profile = Profile(
        constellation="巨蟹座",
        blood_type="B",
        height=180.0,
        weight=85.0
    )
    # 演员3
    a3 = Actor(name="徐峥", nickname="山争哥哥", gender="男")
    a3.profile = Profile(
        constellation="白羊座",
        blood_type="AB",
        height=178.0,
        weight=72.0
    )

    movie1.actors.append(a1)
    movie2.actors.append(a2)
    movie3.actors.append(a3)

    # with get_session() as session:
    #     category_re = CategoryRepository(session)
    #     actor_re = ActorRepository(session)
    #     movie_re = MovieRepository(session)
    #     profile_re = ProfileRepository(session)
    #
    #     category_re.get_all([cate1, cate2, cate3])
    #     movie_re.get_all([movie1, movie2, movie3])
    #     actor_re.get_all([a1, a2, a3])

    """
    4. 	根据主键查询电影信息（包括对应的分类）
    """
    # with get_session() as session:
    #     category_re = CategoryRepository(session)
    #     ar_info = category_re.find_by_id_movie(movie_id=1)
    #     print(ar_info)

    """
    5. 	查询所有的电影（包括对应的分类）
    """
    # with get_session() as session:
    #     category_re = CategoryRepository(session)
    #     ar_info = category_re.find_all_movie_and_category()
    #     print(ar_info)

    """
    6. 	根据主键查询演员信息（包括演员详细资料）
    """
    with get_session() as session:
        category_re = CategoryRepository(session)
        ar_info = category_re.find_by_id_select_actory_and_profile(actor_id=1)
        print(ar_info)

    """
    7. 	查询某个电影及其所有的主演
    """
    # with get_session() as session:
    #     category_re = CategoryRepository(session)
    #     ar_info = category_re.find_by_movie_select_all_movie_actor(movie_id=1)
    #     print(ar_info)

    """
    8. 	查询某个演员演过哪些电影
    """
    with get_session() as session:
        category_re = CategoryRepository(session)
        ar_info = category_re.get_actor_movies(actor_id=1)
        print(ar_info)
