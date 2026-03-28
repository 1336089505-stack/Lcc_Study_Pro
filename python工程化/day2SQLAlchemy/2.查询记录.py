import datetime
from sqlalchemy import (create_engine,MetaData)

engine = create_engine('mysql://root:123456@127.0.0.1:3306/lcc_db',
                       echo=True )#看到sql的动作
meta_data = MetaData()
meta_data.reflect(engine)   #读取表结构

person = meta_data.tables['person'] #获取知道表结构

with engine.connect() as conn:
    # query = person.select() #查询所有
    # results = conn.execute(query)

    # for row in results:
    #     print(row)

    # results_1 = results.fetchall()    #全部
    # print(results_1)

    # row = results.fetchone()    #单条
    # print(row)

    query = person.select().where(person.c.person_birthday < datetime.date(2003,5,16))
    results = conn.execute(query)
    for row in results:
        print(row)




