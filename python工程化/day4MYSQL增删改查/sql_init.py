import pymysql
conn = pymysql.connect(
    host="localhost",
    user="root",         # 你的MySQL用户名
    password="123456",   # 你的MySQL密码
    database="edu_db",  # 数据库名
    charset="utf8mb4",
)

cursor = conn.cursor()