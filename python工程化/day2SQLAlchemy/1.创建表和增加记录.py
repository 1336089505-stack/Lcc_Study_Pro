from sqlalchemy import (create_engine,MetaData,Table,
                        Column,Integer,String,Date)

engine = create_engine('mysql://root:123456@127.0.0.1:3306/lcc_db',
                       echo=True )#看到sql的动作

meta_data = MetaData()

person = Table('person',        #表名
               meta_data,           #metadata对象
               Column('person_id',
                      Integer,
                      primary_key=True,
                      autoincrement=False #取消自增长
                      ),
               Column('person_name',
                      String(150),
                      unique=True,      #唯一
                      nullable=False    #不为空
                      ),
               Column('person_birthday',
                      Date,
                      nullable=False),
               )

meta_data.create_all(engine) #创建

# #insert 一条记录
# person_insert = person.insert() #返回insert语句
# insert_lcc = person_insert.values(person_name = 'lcc' ,
#                                   person_birthday = '2003-8-4')
#
# with engine.connect() as conn:
#     result = conn.execute(insert_lcc)
#     print(result.inserted_primary_key) #可以查询ID
#     conn.commit()

#insert 多条记录
person_insert = person.insert()
with engine.connect() as conn:
    conn.execute(person_insert,[
        {'person_name':'lyx','person_birthday':'2003-3-17'},
        {'person_name':'wxd','person_birthday':'2003-5-14'},    #JSON格式
    ])
    conn.commit()