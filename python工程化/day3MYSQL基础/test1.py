"""
请根据以下描述创建表结构，并添加适当的约束（主键、外键、非空、唯一、检查等）：
1. 部门表（departments）
- 部门ID（dept_id）: 数字类型，主键
- 部门名称（dept_name）: 可变字符串，非空且唯一
- 部门位置（dept_location）: 可变字符串，非空
"""
from sql_init import conn, cursor

sql = "create table if not exists departments(\
  dept_id integer primary key not null comment \"部门ID\",\
  dept_name varchar(255) unique not null comment \"部门名称\",\
  dept_location varchar(255) not null comment \"部门位置\"\
)"
cursor.execute(sql)

"""
员工表（employees）
- 员工ID（emp_id）: 数字类型，主键
- 员工姓名（emp_name）: 可变字符串，非空
- 性别（gender）: 固定长度字符，只能为'M'或'F'
- 出生日期（birth_date）: 日期类型
- 入职日期（hire_date）: 日期类型，非空
- 工资（salary）: 数字类型，大于0
- 部门ID（dept_id）: 数字类型，外键，关联部门表（departments）的部门ID（dept_id）
"""

sql = "create table if not exists employees(\
  emp_id integer primary key not null comment \"员工ID\",\
  emp_name varchar(255) not null comment \"员工姓名\",\
  gender varchar(1) not null check (gender in ('M','F')) comment \"性别\",\
  birth_date date comment \"出生日期\",\
  hire_date date not null comment \"入职日期\",\
  salary integer not null check (salary > 0) comment \"工资\",\
  dept_id integer comment \"关联部门表的部门ID\",\
  foreign key (dept_id) references departments(dept_id)\
)"
cursor.execute(sql)

"""
公司表（companies）
- 公司ID（comp_id）: 数字类型，主键
- 公司名称（comp_name）: 可变字符串，非空且唯一
- 成立日期（found_date）: 日期类型
"""
sql = "create table if not exists companies(\
  comp_id integer primary key not null comment \"公司ID\",\
  comp_name varchar(255) unique not null comment \"公司名称\",\
  dept_location date comment \"成立日期\"\
)"
cursor.execute(sql)

"""
员工公司关系表（emp_comp）用于表示员工在不同公司的工作经历（一个员工可以在多个公司工作过，一个公司也可以有多个员工）
- 记录ID（rec_id）: 数字类型，主键
- 员工ID（emp_id）: 数字类型，外键，关联员工表（employees）的员工ID（emp_id） 删除则置空，更新则同步
- 公司ID（comp_id）: 数字类型，外键，关联公司表（companies）的公司ID（comp_id） 删除和更新都同步
- 开始日期（start_date）: 日期类型
- 结束日期（end_date）: 日期类型，必须大于开始日期（如果结束日期不为空）
"""
sql = "create table if not exists emp_comp(\
  rec_id integer primary key not null comment \"记录ID\",\
  emp_id integer comment \"关联员工表的员工ID\",\
  comp_id integer comment \"关联公司表的公司ID\",\
  start_date date comment \"开始日期\",\
  end_date date comment \"结束日期\",\
  foreign key (emp_id) references employees(emp_id) ON DELETE SET NULL ON UPDATE CASCADE,\
  foreign key (comp_id) references companies(comp_id) ON DELETE CASCADE ON UPDATE CASCADE\
)"
cursor.execute(sql)


cursor.close()
conn.close()