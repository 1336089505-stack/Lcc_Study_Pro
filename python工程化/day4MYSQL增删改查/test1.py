"""
一、建库建表 & 约束（1-8 题）
考点：库表创建、数据类型、主键 / 外键 / 唯一 / 非空 / 默认 / 自增 / 检查约束、索引
"""
# import pymysql
#
# # 连接MySQL（不指定库）
# conn = pymysql.connect(
#     host="localhost",
#     user="root",
#     password="123456",
#     charset="utf8mb4"
# )
# cursor = conn.cursor()
#
# """
# 1.	创建数据库 edu_db，字符集 utf8mb4，排序规则 utf8mb4_general_ci
# """
# sql = """
# CREATE DATABASE IF NOT EXISTS edu_db
# DEFAULT CHARACTER SET utf8mb4
# DEFAULT COLLATE utf8mb4_general_ci
# """
# cursor.execute(sql)


"""
2.	在 edu_db 中创建 student 表：stu_id (INT, 主键，自增)、
stu_name (VARCHAR (50), 非空)、stu_gender (CHAR (1), 
默认 ' 男', 仅允许 ' 男'/' 女 ')、stu_birth (DATE, 非空)、
class_id (INT, 非空)、create_time (DATETIME, 默认当前时间)
"""
from sql_init import conn, cursor
# sql = """
# create table if not exists student(
#   stu_id integer primary key auto_increment not null,
#   stu_name varchar(50) not null,
#   stu_gender char(1) default '男' check (stu_gender in ('男','女')),
#   stu_birth date not null,
#   class_id integer not null,
#   create_time datetime default CURRENT_TIMESTAMP
# )
# """
# cursor.execute(sql)

"""
3.	在 edu_db 中创建 class 表：class_id (INT, 主键，自增)、
class_name (VARCHAR (50), 非空，唯一)、class_teacher (VARCHAR (50), 非空)
、create_time (DATETIME, 默认当前时间)
"""
# sql = """
# create table if not exists class(
#   class_id integer primary key not null,
#   class_name varchar(50) unique not null,
#   class_teacher varchar(50) not null,
#   create_time datetime default CURRENT_TIMESTAMP
# )
# """
# cursor.execute(sql)

"""
4.	为 student 表的 class_id 添加外键，关联 class 表的 class_id，
删除 / 更新班级时级联删除 / 更新学生
"""
# sql = """
# alter table student
# ADD CONSTRAINT fk_student_class
# foreign key (class_id) references class(class_id)
# ON DELETE CASCADE
# ON UPDATE CASCADE;
# """
# cursor.execute(sql)

"""
5.	为 student 表的 stu_name+stu_birth 创建复合唯一索引
"""
# sql = """
# alter table student
# add unique index uk_name_birth (stu_name, stu_birth);
# """
# cursor.execute(sql)

"""
6.	创建 score 表：score_id (INT, 主键，自增)、
stu_id (INT, 非空)、subject_id (INT, 非空)、
score (DECIMAL (5,2), 非空，0~100)、exam_time (DATE, 非空)
"""
# sql = """
# create table if not exists score(
#   score_id integer not null,
#   subject_id integer not null,
#   score decimal(5,2) not null check (score between 0 and 100),
#   exam_time date not null
# )
# """
# cursor.execute(sql)

"""
7.	创建 subject 表：subject_id (INT, 主键，自增)、
subject_name (VARCHAR (50), 非空，唯一)、subject_type (VARCHAR (20), 
默认 ' 必修 ', 仅允许 ' 必修 '/' 选修 ')
"""
# sql = """
# create table if not exists subject(
#   subject_id integer primary key auto_increment not null,
#   subject_name varchar(50) unique not null,
#   subject_type varchar(20) default '必修' check (subject_type in ('必修','选修'))
# )
# """
# cursor.execute(sql)

"""
8.	为 score 表的 score 字段添加检查约束（0≤score≤100）
"""
# sql = """
# alter table score
# add constraint score check (score between 0 and 100);
# """
# cursor.execute(sql)

"""
二、增删改操作（9-15 题）
考点：INSERT/UPDATE/DELETE、批量操作、条件修改 / 删除、字段计算
"""

"""
1.	向 class 表插入 3 条数据：(1,' 高一 (1) 班 ',' 张老师 ')、
(2,' 高一 (2) 班 ',' 李老师 ')、(3,' 高一 (3) 班 ',' 王老师 ')
"""
# sql = """INSERT INTO class(class_id, class_name, class_teacher)
#     VALUES (1, '高一 (1) 班 ', '张老师'),
#     (2, '高一 (2) 班', '李老师'),
#     (3, '高一 (3) 班', '王老师')
#     """
# cursor.execute(sql)
# conn.commit()

"""
2.	向 student 表批量插入 5 条数据（匹配 class_id）：
(NULL,' 小明 ',' 男 ','2008-01-10',1,NOW ())、
(NULL,' 小红 ',' 女 ','2008-02-15',1,NOW ())、
(NULL,' 小刚 ',' 男 ','2008-03-20',2,NOW ())、
(NULL,' 小丽 ',' 女 ','2008-04-25',2,NOW ())、
(NULL,' 小亮 ',' 男 ','2008-05-30',3,NOW ())
"""
# sql = """INSERT INTO student(stu_id,stu_name,stu_gender,stu_birth,class_id,create_time)
#     VALUES (NULL,'小明','男','2008-01-10',1,NOW()),
#     (NULL,'小红','女','2008-02-15',1,NOW()),
#     (NULL,'小刚','男','2008-03-20',2,NOW()),
#     (NULL,'小丽','女','2008-04-25',2,NOW()),
#     (NULL,'小亮','男','2008-05-30',3,NOW())
#     """
# cursor.execute(sql)
# conn.commit()

"""
3.	向 subject 表插入 3 条数据：(NULL,' 数学 ',' 必修 ')、
(NULL,' 语文 ',' 必修 ')、(NULL,' 英语 ',' 必修 ')
"""
# sql = """INSERT INTO subject(subject_id,subject_name,subject_type)
#     VALUES (NULL,'数学','必修'),
#     (NULL,'语文','必修'),
#     (NULL,'英语','必修')
#     """
# cursor.execute(sql)
# conn.commit()

"""
4.	向 score 表插入学生成绩（每个学生 3 门科目，分数 60~100 随机）
"""
# sql = """INSERT INTO score(score_id,subject_id,score,exam_time)
#     SELECT
#     s.stu_id,
#     sub.subject_id,
#     ROUND(60 + (RAND() * 40), 2),
#     '2024-01-15'
#     FROM student s
#     CROSS JOIN subject sub;
#     """
# cursor.execute(sql)
# conn.commit()

"""
5.	将高一 (1) 班的班主任修改为赵老师，并更新 create_time 为当前时间
"""
# sql = """update class
#     set class_teacher = '赵老师',
#     create_time = now()
#     where class_id = 1
#     """
# cursor.execute(sql)
# conn.commit()

"""
6.	删除高一 (3) 班中性别为女的学生数据
"""
# sql = """delete from student
#     where stu_gender = "女" and class_id = 3
#     """
# cursor.execute(sql)
# conn.commit()

"""
7.	将所有学生的数学成绩加 5 分（最高不超过 100 分）
"""
# sql = """update score
#     set score = least(score + 5 , 100 )
#     where subject_id = 1
#     """
# cursor.execute(sql)
# conn.commit()

"""
三、关联查询（16-22 题）
考点：内连接 / 左连接 / 右连接 / 全连接、多表关联、分组聚合、行转列
4.	查询高一 (2) 班所有学生的语文、数学、英语成绩（行转列，显示为三列）
5.	左连接 student 和 score，查询没有成绩的学生姓名
6.	按科目分组，查询每个科目的平均分、最高分、最低分
7.	模拟全连接，查询所有班级和所有学生（含无学生的班级、无班级的学生）
"""

"""
1.	内连接 student 和 class，查询学生姓名、班级名称、班主任
"""
# sql = """select
#     stu.stu_name,cla.class_name,cla.class_teacher
#     from student stu
#     inner join class cla on cla.class_id = stu.class_id
#     """
# cursor.execute(sql)
# results = cursor.fetchall()
# for row in results:
#     print(row)

"""
2.	按班级分组，查询每个班级的学生人数，按人数降序排列
"""
# sql = """
#     select
#         cla.class_id,
#         cla.class_name,
#         count(stu.stu_id) as stu_count
#     from student stu
#     inner join class cla on cla.class_id = stu.class_id
#     group by cla.class_id, cla.class_name
#     order by stu_count desc;
#     """
# cursor.execute(sql)
# results = cursor.fetchall()
# for row in results:
#     print(row)

"""
3.	关联 student、subject、score 三张表，查询学生姓名、科目名称、分数
"""
sql = """
    select 
        stu.stu_name,
        sub.subject_name,
        sco.score
    from score sco
    inner join student stu on stu.stu_id = sco.score_id
    inner join subject sub on sub.subject_id = sco.subject_id
    """
cursor.execute(sql)
results = cursor.fetchall()
for row in results:
    print(row)

cursor.close()
conn.close()
