"""
根据需求创建表结构，包含信息有：
学生姓名
年龄
性别
籍贯地区
出生日期
班级名称
科目名称
科目成绩
科目老师姓名
"""
from sqlalchemy import (create_engine, MetaData, Table,
                        Column, Integer, String, Date, ForeignKey)

engine = create_engine('mysql://root:123456@127.0.0.1:3306/lcc_db',
                       echo=True )#看到sql的动作

meta_data = MetaData()

student_class = Table('student_class',meta_data,
                     Column('id',
                            Integer,
                            primary_key=True,
                            autoincrement=False),
                     Column('class_name',
                            String(50),
                            nullable=False)
                      )

student_info = Table('student_info',meta_data,
                     Column('student_id',
                            Integer,
                            primary_key=True,
                            autoincrement=False),
                     Column('student_name',
                            String(50),
                            nullable=False),
                     Column('student_age',
                            Integer,
                            nullable=False),
                     Column('student_gender',
                            String(10),
                            nullable=False),
                     Column('student_country',
                            String(100),
                            nullable=False),
                     Column('student_birthday',
                            Date,
                            nullable=False),
                     Column('class_id',
                            Integer,
                            ForeignKey("student_class.id"))
                     )


subject_info = Table('subject_info',
                     meta_data,
                     Column('id',
                            Integer,
                            primary_key=True,
                            autoincrement=False),
                     Column('subject_name',
                            String(50),
                            nullable=False),
                    Column('subject_teacher_name',
                            String(50),
                            nullable=False)
                      )

subject_score = Table('subject_score',
                     meta_data,
                     Column('student_id',
                            Integer,
                            ForeignKey("student_info.student_id")),
                     Column('subject_id',
                            Integer,
                            ForeignKey("subject_info.id")),
                     Column('score',
                            Integer,
                            nullable=False)
                    )

meta_data.create_all(engine)

