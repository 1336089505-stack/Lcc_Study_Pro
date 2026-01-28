"""
闰年判断器：
1. 用户输入年
2. 判断同时满足被4整除且不被100整除，或者被400整除，则输出“闰年”，否则输出“平年”
"""

"""
year_input = input("输入年:")
try:
    year = int(year_input)
except ValueError:
    print("请输入整数")
    exit()

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"{year}是闰年")
else:
    print(f"{year}是平年")
"""


"""
编写程序判断一个数是否为质数：
1. 提示用户输入一个正整数
2. 使用while循环检查该数是否为质数
3. 质数定义：只能被1和自身整除的大于1的自然数
4. 输出判断结果
5. 要求优化循环次数（只需检查到sqrt(n)）
"""
"""
from math import sqrt

num_input = input("输入正整数:")
try:
    num = int(num_input)
except ValueError:
    print("请输入正整数")
    exit()

check = True
if num == 1:
    check = False
elif num == 2:
    check = True
elif num % 2 == 0:
    check = False
else:
    num_s = int(sqrt(num)) + 1
    i = 3
    while i < num_s:
        if num % i == 0:
            check = False
        i += 2
        
if check:
    print("是质数")
elif not check:
    print("不是质数")
"""

"""
编写猜数字游戏：
1. 程序随机生成1-100之间的整数
2. 用户有最多7次猜测机会
3. 每次猜测后提示"太大"、"太小"或"正确"
4. 猜对或用完机会后显示结果和实际数字
5. 使用while循环和break控制流程
"""
"""
import random
num = random.randint(1, 100)
i = 7
while i > 0:
    num_guess = int(input(f"第{7-i+1}猜测："))
    if num_guess > num:
        print("太大")
    elif num_guess < num:
        print("太小")
    elif num_guess == num:
        print("猜对了！")
        exit()
    i -= 1
print("机会用完了，数字是{}".format(num))
"""

"""
生成斐波那契数列：
1. 提示用户输入要生成的数列长度
2. 使用while循环生成斐波那契数列
3. 数列定义：F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2)
4. 输出生成的数列
5. 要求支持生成任意长度的数列
"""

"""
len = int(input("输入要生成的数列长度："))
list_f = []
if len == 1:
    list_f = [0]
else:
    list_f = [0, 1]

i = 2
while i < len:
    num_temp = list_f[i-1] + list_f[i-2]
    list_f.append(num_temp)
    i += 1
print(list_f)
"""

"""
编写密码验证系统：
1. 预设正确密码为"Python123"
2. 用户有3次尝试机会
3. 每次输入密码后验证，正确则欢迎，错误提示剩余次数
4. 3次错误后锁定账户
5. 使用while循环和continue/break控制
"""

"""
password = 'Python123'
i = 3
check = True
while i > 0:
    new_password = input("输入密码:")
    if password != new_password:
        i -= 1
        check = False
    if check:
        print("密码正确")
        break
    else:
        print("密码错误")
if i == 0:
    print("----锁定账户----")
"""

"""
编写简单表达式计算器：
1. 支持+、-、*、/四种运算
2. 用户输入格式：数字1 运算符 数字2
3. 使用while循环让用户可以连续计算
4. 输入"quit"退出程序
5. 处理除零错误和无效输入
"""
while True:
    nums_input = input("输入格式：数字1 运算符 数字2：")
    if nums_input == "quit":
        print("退出程序")
        break
    else:
        nums = nums_input.split(" ")
        try:
            num1 = float(nums[0])
            num2 = float(nums[2])
        except ValueError:
            print("输入正确数字：")
            continue
        if nums[1] == "+":
            print("num1 + num2 =", num1 + num2)
        elif nums[1] == "-":
            print("num1 - num2 =", num1 - num2)
        elif nums[1] == "*":
            print("num1 - num2 =", num1 * num2)
        elif nums[1] == "/":
            try:
                print("num1 / num2 =", num1 / num2)
            except ZeroDivisionError:
                print("除零错误")
        else:
            print("输入正确运算符")


