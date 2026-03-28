from sqlalchemy import (create_engine,MetaData,Table,
                        Column,Integer,String,Date)

engine = create_engine('mysql://root:123456@127.0.0.1:3306/lcc_db',
                       echo=True )#看到sql的动作




if __name__ == '__main__':

    pass