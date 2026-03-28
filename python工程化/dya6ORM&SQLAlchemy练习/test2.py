"""
本题基于前一作业的电商系统，基于Pymsql组件封装自己的BaseDAO，并用BaseDAO查询用户表：
1、编写BaseDAO
2、使用BaseDAO查询用户表数据
"""
import pymysql

class BaseDAO:
    @staticmethod
    def get_conn():
        conn = pymysql.connect(
            host="localhost",
            user="root",  # 你的MySQL用户名
            password="123456",  # 你的MySQL密码
            database="day6_mysql",  # 数据库名
            charset="utf8mb4",
        )
        return conn

    @staticmethod
    def query(sql, args=None):
        conn = None
        cursor = None
        try:
            conn = BaseDAO.get_conn()
            cursor = conn.cursor()
            cursor.execute(sql, args)
            return cursor.fetchall()  # 返回所有结果
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()