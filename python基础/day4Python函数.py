"""
编写一个包含多个数学计算函数的程序：
1.	实现计算阶乘的函数factorial(n)
2.	实现判断素数的函数is_prime(n)
3.	实现计算最大公约数的函数gcd(a, b)
4.	实现计算斐波那契数列的函数fibonacci(n)
5.	实现一个主函数，提供菜单让用户选择要使用的功能
6.	每个函数都要有详细的文档字符串说明
"""



def factorial(n):
    """
    计算阶乘
    :param n:
    """
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


from math import sqrt
def is_prime(n):
    """
    判断素数
    :param n:
    """
    check = True
    if n == 1:
        check = False
    elif n == 2:
        check = True
    elif n % 2 == 0:
        check = False
    else:
        n_s = int(sqrt(n)) + 1
        i = 3
        while i < n_s:
            if n % i == 0:
                check = False
            i += 2
    if check:
        return "是质数"
    else:
        return "不是质数"

def gcd(a, b):
    """
    计算最大公约数
    :param a:
    :param b:
    """
    min_num = min(a, b)
    i = 1
    max_gcd = 0
    while i <= min_num:
        if a % i == 0 and b % i == 0:
            max_gcd = i
        i += 1
    return max_gcd

def fibonacci(n):
    """
    计算斐波那契数列的函数
    :param n:
    :return:
    """
    if n == 1:
        list_f = [0]
    else:
        list_f = [0, 1]
    i = 2
    while i < n:
        num_temp = list_f[i - 1] + list_f[i - 2]
        list_f.append(num_temp)
        i += 1
    return list_f

def main_menu1():
    """
    主菜单
    :return:
    """
    while True:
        print("             ----菜单----      ")
        print("    1.实现计算阶乘的函数factorial(n)\n\
    2.实现判断素数的函数is_prime(n)\n\
    3.实现计算最大公约数的函数gcd(a, b)\n\
    4.实现计算斐波那契数列的函数fibonacci(n)")
        n = input("请选择功能:")
        match n:
            case '1':
                print("计算阶乘factorial(n)")
                num = input("请输入正整数:")
                print(factorial(int(num)))
            case '2':
                print("判断素数is_prime(n)")
                num = input("请输入正整数:")
                print(is_prime(int(num)))
            case '3':
                print("计算最大公约数gcd(a, b)")
                num1 = input("请输入整数a:")
                num2 = input("请输入整数a:")
                print(gcd(int(num1), int(num2)))
            case '4':
                print("计算斐波那契数列fibonacci(n)")
                num = input("请输入正整数:")
                print(fibonacci(n))

"""
编写一个字符串处理工具集，包含以下函数：
1.	统计字符串中各种字符类型的数量（字母、数字、空格、其他）
2.	检查字符串是否为回文（正读反读都一样）
3.	将字符串中的单词反转顺序
4.	统计每个单词出现的频率
5.	将字符串转换为标题格式（每个单词首字母大写）
6.	主函数提供交互式菜单供用户选择功能
"""
def str_style_count(strs):
    """
    统计字符串中各种字符类型的数量（字母、数字、空格、其他）
    :param strs:
    :return:
    """
    space_num, eng_num, math_num, other_num = 0, 0, 0, 0
    for ch in strs:
        if ord(ch) == 32:
            space_num += 1
        elif 48 <= ord(ch) <= 57:
            math_num += 1
        elif 65 <= ord(ch) <= 90 or 97 <= ord(ch) <= 122:
            eng_num += 1
        else:
            other_num += 1
    return space_num, eng_num, math_num,other_num

def is_str_palindromic(strs):
    """
    检查字符串是否为回文
    :param strs:
    :return:
    """
    if strs == strs[::-1]:
        return True
    else:
        return False


def str_reverse(strs):
    """
    将字符串中的单词反转顺序
    :param strs:
    :return:
    """
    strs_tmp = strs[::-1]
    return strs_tmp

def word_cont(strs):
    """
    统计每个单词出现的频率
    :param strs:
    :return:
    """
    str_tmp = strs.split()
    words_ct = {}
    for word in str_tmp:
        words_ct[word] = words_ct.get(word, 0) + 1
    return words_ct

def str_head(strs):
    """
    将字符串转换为标题格式（每个单词首字母大写）
    :param strs:
    :return:
    """
    return strs.title()

def main_menu2():
    """
    主菜单
    :return:
    """
    while True:
        print("             ----菜单----      ")
        print("1.统计字符串中各种字符类型的数量（字母、数字、空格、其他)\n\
2.检查字符串是否为回文（正读反读都一样）\n\
3.将字符串中的单词反转顺序\n\
4.统计每个单词出现的频率\n\
5.将字符串转换为标题格式（每个单词首字母大写）")
        n = input("请选择功能:")
        match n:
            case '1':
                print("统计字符串中各种字符类型的数量（字母、数字、空格、其他)")
                strs = input("请输入字符串:")
                print("空格:%d个,字母:%d个,数字:%d个,其他:%d个"%str_style_count(strs))
            case '2':
                print("检查字符串是否为回文（正读反读都一样）")
                strs = input("请输入字符串:")
                if is_str_palindromic(strs):
                    print("是回文")
                else:
                    print("不是回文")
            case '3':
                print("将字符串中的单词反转顺序")
                strs = input("请输入字符串:")
                print("反转为",str_reverse(strs))
            case '4':
                print("统计每个单词出现的频率")
                strs = input("请输入字符串:")
                print(word_cont(strs))
            case '5':
                print("将字符串转换为标题格式（每个单词首字母大写）")
                strs = input("请输入字符串:")
                print(str_head(strs))

"""
使用函数重构学生成绩管理系统：
1. 	使用字典存储学生信息，键为学号，值为包含姓名和成绩的字典
2. 	实现添加、删除、修改、查询、统计、排序等功能函数
3. 	每个函数职责单一，参数和返回值明确
4. 	使用函数实现自定义排序（选做）
5. 	主函数提供完整的用户交互界面
"""
from typing import Union

student_info : dict[int,dict[str,Union[str, int]]]= {
    1:{"姓名":"李1","成绩":11},
    2:{"姓名":"李2","成绩":21},
    3:{"姓名":"李3","成绩":31},
    4:{"姓名":"李4","成绩":41}
}

def add_student_info(student_dict:dict[int,dict[str,Union[str, int]]]):
    """
    添加学生信息
    :param student_dict:
    :return:
    """
    student_info.update(student_dict)

def update_student_info(student_id:int,name:str = None,score:int = None):
    """
    修改学生信息
    :param student_id:
    :param name:
    :param score:
    :return:
    """
    for student in student_info:
        if student == student_id:
            if name is not None:
                student_info[student]["姓名"] = name
            if score is not None:
                student_info[student]["成绩"] = score

def select_student_info(name_or_id:Union[int,str]):
    """
    查询学生信息
    :param name_or_id:
    :return:
    """
    try:
        if type(name_or_id) is int:
            return {name_or_id:student_info[name_or_id]}
        else:
            students = {}
            for student in student_info.keys():
                if student_info[student]["姓名"] == name_or_id:
                    students.update({student:student_info[student]})
                    return students
    except KeyError:
        print(f"查询不到{name_or_id}信息")
        return None

def del_student_info(name_or_id:Union[int,str]):
    """
    删除学生信息
    :param name_or_id:
    :return:
    """
    student_info_tmp = select_student_info(name_or_id)
    for student in student_info_tmp.keys():
        del student_info[student]

def count_student_info(score_min:int = 0,score_max:int = 100):
    """
    统计分数区间的学生信息
    :param score_min:
    :param score_max:
    :return:
    """
    student_info_tmp = {}
    for student in student_info.keys():
        score = student_info[student]["成绩"]
        if score_min <= score <= score_max:
            student_info_tmp.update({student:student_info[student]})
    return student_info_tmp

def sort_student_info():
    """
    成绩排序
    :return:
    """
    score_list = []
    for student in student_info.keys():
        score_list.append(student_info[student]["成绩"])
    score_list.sort(reverse=True)
    student_info_tmp = {}
    for score in score_list:
        for student in student_info.keys():
            student_score = student_info[student]["成绩"]
            if score == student_score:
                student_info_tmp.update({student:student_info[student]})

    return student_info_tmp


def main_menu3():
    """
    主菜单
    :return:
    """
    while True:
        print("----菜单----")
        print("1.添加学生信息"
              "2.删除学生信息"
              "3.修改学生信息"
              "4.查询学生信息"
              "5.统计学生信息"
              "6.排序学生信息")
        n = input("请选择功能:")
        match n:
            case '1':
                add_student_info({5: {"姓名": "李5", "成绩": 51}})
                add_student_info({6: {"姓名": "李6", "成绩": 61}})
                print(student_info)
            case '2':
                name_or_id = input("请输入删除学生信息的学号或名字:")
                try:
                    name_or_id = int(name_or_id)
                    del_student_info(name_or_id)
                except ValueError:
                    del_student_info(name_or_id)
                print(student_info)
            case '3':
                student_id = int(input("请输入学生信息的学号:"))
                name = input("修改学生信息的名字（不输入不修改）:")
                score = int(input("修改学生信息的成绩（不输入不修改）:"))
                update_student_info(student_id, name, score)
                print(student_info)
            case '4':
                name_or_id = input("请输入查询学生信息的学号或名字:")
                try:
                    name_or_id = int(name_or_id)
                    print(select_student_info(name_or_id))
                except ValueError:
                    print(select_student_info(name_or_id))
            case '5':
                try:
                    score_min = int(input("统计学生成绩最小值（不输入默认0）:"))
                except ValueError:
                    score_min = 0
                try:
                    score_max = int(input("统计学生成绩最大值（不输入默认100）:"))
                except ValueError:
                    score_max = 100
                print(count_student_info(score_min, score_max))
            case '6':
                print(sort_student_info())

"""
题目4：图形打印函数集
编写一组图形打印函数：
1. 	打印直角三角形
2. 	打印等腰三角形
3. 	打印菱形
4. 	打印空心正方形
5. 	打印乘法表
6. 	每个函数接受参数控制图形大小和使用的字符
7. 	使用默认参数和关键字参数提高灵活性
8. 	主函数让用户选择要打印的图形
"""
def print_right_triangle(size, char):
    """
    打印直角三角形
    :param size:
    :param char:
    """
    if size < 1:
        print("图形大小不能小于1！")
        return
    print("\n直角三角形：")
    for i in range(1, size + 1):
        print(char * i)


def print_isosceles_triangle(size, char):
    """
    打印等腰三角形
    :param size:
    :param char:
    """
    if size < 1:
        print("图形大小不能小于1！")
        return
    print("\n等腰三角形：")
    for i in range(0, size + 1):
        print(' ' * (len(char)*size - i*len(char)), end='')
        print(char * (2 * i -1))

def print_diamond(size, char):
    """
    打印菱形
    :param size: 菱形的大小（上半部分行数），默认值为5
    :param char: 组成菱形的字符，默认值为'*'
    """
    if size < 1:
        print("图形大小不能小于1！")
        return
    print("\n菱形：")
    for i in range(1, size + 1):
        print(' ' * (size - i), end='')
        print(char * (2 * i - 1))
    for i in range(size - 1, 0, -1):
        print(' ' * (size - i), end='')
        print(char * (2 * i - 1))

def print_hollow_square(size, char):
    """
    打印空心正方形
    :param size:
    :param char:
    """
    if size < 1:
        print("图形大小不能小于1！")
        return
    print("\n空心正方形：")
    for i in range(size):
        for j in range(size):
            if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                print(char+"  ", end='')
            else:
                print(' '+"  ", end='')
        print()


def print_multiplication_table(size, char):
    """
    打印乘法表
    :param size:
    :param char:
    """
    if size < 1 :
        print("乘法表大小不能小于1")
        return
    print("\n乘法表：")
    for i in range(1, size + 1):
        for j in range(1, i + 1):
            product = i * j
            print(f"{j}×{i}={product}{char}", end='')
        print()

def main_menu4():
    """
       主菜单
       :return:
       """
    while True:
        print("----菜单----")
        print("1.打印直角三角形\n"
              "2.打印等腰三角形\n"
              "3.打印菱形\n"
              "4.打印空心正方形\n"
              "5.打印乘法表\n")
        n = input("请选择功能:")
        match n:
            case '1':
                size_num = int(input("请输入大小"))
                draw_str = input("请输入绘制字符")
                print_right_triangle(size_num, draw_str)
            case '2':
                size_num = int(input("请输入大小"))
                draw_str = input("请输入绘制字符")
                print_isosceles_triangle(size_num, draw_str)
            case '3':
                size_num = int(input("请输入大小"))
                draw_str = input("请输入绘制字符")
                print_diamond(size_num, draw_str)
            case '4':
                size_num = int(input("请输入大小"))
                draw_str = input("请输入绘制字符")
                print_hollow_square(size_num, draw_str)
            case '5':
                size_num = int(input("请输入大小"))
                draw_str = input("请输入间隔字符")
                print_multiplication_table(size_num, draw_str)

"""
题目5：个人财务管理模块
编写一个模块 finance_manager.py，包含以下功能：
1.	先定义一个全局的列表对象users，列表中存储多个用户字典，每个用户字典有：用户名（username）、密码（password）、余额（blance）、是否登录(isLogin，初始化为False)。
2.	实现一个注册方法，提示输入用户名和密码，然后检查用户名是否被注册，如果已注册则提示。如果没有注册，则往列表对象添加一个用户，存储用户名、密码、余额(使用500-1000随机数)、是否登录(初始化为False)。
3.	并设置一个全局str变量“current_login_user”，默认值为None。
4.	实现登录方法，判断用户是否在列表中，如果不在则提示，如果在则验证密码是否正确，如果正确，将“是否登录”置为True。将登录的用户名写到current_login_user变量中。
5.	实现登录检查方法，判断current_login_user存储的用户名，和对应的字典中的isLogin是否为True。
6.	实现方法：add_transaction(amount, category, description) 添加交易记录。方法执行前要调用登录检查。
    实现方法：get_balance() 计算并返回当前余额。方法执行前要调用登录检查。
7.	实现方法：get_summary_by_category() 按类别汇总交易金额。方法执行前要调用登录检查。
8.	实现登录注销方法：，在users列表中按current_login_user中存储的用户名找到对应的字典，将其中的isLogin设为False，将current_login_user变量设为None。
9.	实现退出方法，程序直接退出。注意：登录注销不能退出程序，主菜单可以继续选择功能。
10.	编写主程序使用这个模块，提供简单的菜单界面。
"""
users = {
    1:{"username":"admin", "password":"111111","balance":111,"isLogin":False},
    2:{"username":"admin2", "password":"222222","balance":222,"isLogin":False},
    3:{"username":"admin3", "password":"333333","balance":333,"isLogin":False},
    4:{"username":"admin4", "password":"444444","balance":444,"isLogin":False},
    5:{"username":"admin5", "password":"555555","balance":555,"isLogin":False},
}
current_login_user = None
transaction = []
import random

def sign_up(p_username:str,p_password:str):
    """
    用户注册
    :param p_username:
    :param p_password:
    :return:
    """
    for user in users:
        if users[user]["username"] == p_username:
            print("该用户已注册")
            return
    users.update({len(users)+1:{"username":p_username,"password":p_password,"balance":random.randint(500, 1000),"isLogin":False}})

def log_in(p_username:str,p_password:str):
    """
    登录
    :param p_username:
    :param p_password:
    :return:
    """
    for user in users:
        if users[user]["username"] != p_username:
            pass
        else:
            if users[user]["password"] == p_password:
                users[user]["isLogin"] = True
                global current_login_user
                current_login_user = users[user]["username"]
                print("登录成功")
                return
    print("用户未注册")

def check_log_in():
    """
    判断登录
    :return:
    """
    global current_login_user
    for user in users:
        if users[user]["username"] == current_login_user:
            if users[user]["isLogin"] == True:
                print(f"当前用户{current_login_user}已登录")
                return True
            else:
                print(f"当前用户{current_login_user}未登录")
                return False
    return False

#金额类别描述
def add_transaction(amount:int, category:str, description:str):
    """
    添加交易记录。方法执行前要调用登录检查
    :param amount:
    :param category:
    :param description:
    :return:
    """
    if not check_log_in():
        return
    for user in users:
        if users[user]["username"] == current_login_user:
            transaction.append([amount,category,description])
            print("添加交易记录成功")
            return


def get_balance(current_balance:int,current_category:str)->int:
    """
    计算并返回当前余额
    :return:
    """
    all_balance = current_balance
    for tra in transaction:
        if current_category == tra[2]:
            all_balance = all_balance + tra[1]
    return all_balance

def get_summary_by_category(category:str):
    """
    按类别汇总交易金额。方法执行前要调用登录检查。
    :return:
    """
    if not check_log_in():
        return
    for user in users:
        if users[user]["username"] == current_login_user:
            users[user]["balance"] = get_balance(users[user]["balance"],category)

def log_out():
    """
    注销登录
    :return:
    """
    global current_login_user
    for user in users:
        if users[user]["username"] == current_login_user:
            users[user]["isLogin"] = False
            current_login_user = None
            return

def main_menu5():
    """
       主菜单
       :return:
    """
    while True:
        print("----菜单----")
        print("1.用户注册\n"
              "2.登录用户\n"
              "3.添加交易记录\n"
              "4.按类别汇总交易金额\n"
              "5.注销用户\n"
              "6.退出\n")
        n = input("请选择功能:")
        match n:
            case '1':
                p_username = input("请输入用户名")
                p_password = input("请输入密码")
                sign_up(p_username,p_password)
            case '2':
                p_username = input("请输入用户名")
                p_password = input("请输入密码")
                log_in(p_username, p_password)
            case '3':
                add_transaction(500,'1','111111')
                add_transaction(-200, '1', '111111111111')
                add_transaction(300, '3', '33333333')
            case '4':
                get_summary_by_category(category='1')
            case '5':
                log_out()
            case '6':
                exit()


if __name__ == '__main__':
    #第一题
    #main_menu1()

    #第二题
    #main_menu2()

    #第三题
    #main_menu3()

    #第四题
    #main_menu4()

    # 第五题
    main_menu5()


    pass