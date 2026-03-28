from session import get_session,engine
from model import Category,Movie,Actor,MovieActor,Profile,Base
if __name__ == '__main__':
    """
    1.	创建数据库表
    """
    Base.metadata.create_all(engine)




    pass