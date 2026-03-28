"""
向部门表插入以下数据（5分）：
- 部门ID: 1, 部门名称: '技术部', 部门位置: '北京'
- 部门ID: 2, 部门名称: '市场部', 部门位置: '上海'
- 部门ID: 3, 部门名称: '人力资源部', 部门位置: '广州'
"""
from sql_init import conn, cursor

# sql = "INSERT INTO departments(dept_id, dept_name, dept_location)\
#     VALUES (1, '技术部', '北京'),(2, '市场部', '上海'),(3, '人力资源部', '广州')"
# cursor.execute(sql)
# conn.commit()

"""
2. 向员工表插入以下数据（5分）：
- 员工ID: 101, 姓名: '张三', 性别: 'M', 出生日期: '1990-01-01', 入职日期: '2015-06-01', 工资: 15000, 部门ID: 1
- 员工ID: 102, 姓名: '李四', 性别: 'F', 出生日期: '1992-05-12', 入职日期: '2016-07-15', 工资: 12000, 部门ID: 2
- 员工ID: 103, 姓名: '王五', 性别: 'M', 出生日期: '1988-11-20', 入职日期: '2014-03-10', 工资: 18000, 部门ID: 1
"""
# sql = "INSERT INTO employees(emp_id, emp_name, gender,birth_date,hire_date,salary,dept_id)\
# VALUES (101, '张三', 'M','1990-01-01','2015-06-01',15000,1),\
#        (102, '李四', 'F','1992-05-12','2016-07-15',12000,2),\
#        (103, '王五', 'M','1988-11-20','2014-03-10',18000,1)"
# cursor.execute(sql)
# conn.commit()

"""
3. 向公司表插入以下数据（5分）：
- 公司ID: 1001, 公司名称: '阿里巴巴', 成立日期: '1999-01-01'
- 公司ID: 1002, 公司名称: '腾讯', 成立日期: '1998-11-11'
"""
# sql = "INSERT INTO companies(comp_id, comp_name,dept_location)\
# VALUES (1001, '阿里巴巴', '1999-01-01'),\
#        (1002, '腾讯', '1998-11-11')"
# cursor.execute(sql)
# conn.commit()


"""
4. 向员工公司关系表插入以下数据（5分）：
- 记录ID: 1, 员工ID: 101, 公司ID: 1001, 开始日期: '2015-06-01', 结束日期: '2018-05-31'
- 记录ID: 2, 员工ID: 101, 公司ID: 1002, 开始日期: '2018-06-01', 结束日期: null (表示至今仍在职)
- 记录ID: 3, 员工ID: 102, 公司ID: 1001, 开始日期: '2016-07-15', 结束日期: null
注意：日期格式使用'YYYY-MM-DD'
"""
sql = ("INSERT INTO emp_comp(rec"
       "_id, emp_id,comp_id,start_date,end_date)\
VALUES (1,101,1001,'2015-06-01','2018-05-31'),\
       (2,101,1002,'2018-06-01',null),\
       (3,102,1001,'2016-07-15',null)")
cursor.execute(sql)
conn.commit()






cursor.close()
conn.close()