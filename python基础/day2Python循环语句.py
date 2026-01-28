"""
编写一个程序，根据用户输入的数字n，打印一个数字金字塔。要求：
•用户输入一个正整数n（1 ≤ n ≤ 9）
•金字塔第一行有1个数字，第二行有2个数字，以此类推，第n行有n个数字
•每行的数字从1开始递增，例如第3行是"123"
•金字塔需要居中对齐（使用空格进行缩进）
•使用嵌套循环实现
示例（n=4）：
   1
  12
 123
1234
"""

"""
num = int(input("输入一个正整数n（1 ≤ n ≤ 9）:"))
print_str = ""
i = 1
while i <= num:
    print_str = " " * (num-i)
    n = 1
    while n <= i:
        print_str += str(n)
        n += 1
    print(print_str)
    i += 1
"""

"""
编写程序查找10000以内的所有完美数：
1. 完美数定义：等于其所有真因子（不包括自身）之和的数
2. 例如：6 = 1 + 2 + 3
3. 使用嵌套循环实现
4. 输出找到的所有完美数

示例输出：6, 28, 496, 8128
"""
"""
str_num = ""
for i in range(1,10000):
    sum = 0
    for j in range(1,i):
        if i % j == 0:
            sum += j
    if i == sum:
        str_num += str(i)
        str_num += ","
print(str_num)"""

"""
查找100以内的所有素数对：
1. 素数对定义：相差2的两个素数，如(3,5)、(5,7)
2. 先找出100以内的所有素数
3. 再找出所有相差2的素数对
4. 使用循环和条件判断实现
5. 输出所有素数对

示例输出：
(3, 5)
(5, 7)
(11, 13)
...
"""
"""
from math import sqrt
num_list = [2]
for num in range(3,100):
    check = True
    if num % 2 == 0:
        check = False
    else:
        num_s = int(sqrt(num)) + 1
        i = 3
        while i < num_s:
            if num % i == 0:
                check = False
                break
            i += 2
    if check:
        num_list.append(num)
count = len(num_list)
i = 0
while i < count-1:
    if (num_list[i+1]-num_list[i]) == 2:
        print(f"({num_list[i]},{num_list[i+1]})")
    i += 1
"""

"""
任务描述： 你正在为一款新型工业级无人机开发控制系统的指令解析模块。无人机通过地面站发送字符串指令，你需要编写一个程序，能够持续接收指令并利用 Python 的 match-case 结构进行精准解析与解构。
功能要求：
1.	持续监听： 程序需使用 while True 循环持续接收用户输入。
2.	指令解构：
o	单字指令： 如果输入为 takeoff，输出 系统：正在启动动力系统，准备起飞。；如果输入为 land，输出 系统：正在自动寻迹降落。 并终止循环。
o	双字指令（动作 + 数值）： 能够匹配类似 up 10、down 20、speed 5 的指令。要求解构出动作名和数值，并输出 执行：[动作名]，目标参数：[数值]。
o	带约束的指令（模式守卫）： 如果动作是 move，后面需跟 方向 和 距离（如 move left 50）。请利用 if 守卫模式确保距离必须是纯数字字符串。若校验通过，输出 航向修正：向[方向]移动[距离]米。
3.	容错处理： 对于任何不符合上述格式的输入，输出 警告：无法识别的非法指令序列，请重新输入。
输入与输出用例预览：
•	用例 1（单字指令）： 
o	输入：takeoff 
o	输出：“系统：正在启动动力系统，准备起飞。”
•	用例 2（解构指令）： 
o	输入：speed 80 
o	输出：“执行：speed，目标参数：80。”
•	用例 3（模式守卫）： 
o	输入：move north 100 
o	输出：“航向修正：向north移动100米。”
•	用例 4（非法输入）： 
o	输入：move north high （注：距离不是数字） 
o	输出：“警告：无法识别的非法指令序列，请重新输入。”
•	用例 5（退出）： 
o	输入：land 
o	输出：“系统：正在自动寻迹降落。” （程序结束）
"""
"""
while True:
    command = input("输入指令:")
    command_list = command.split(" ")
    match command_list[0]:
        case "takeoff":
            print("系统：正在启动动力系统，准备起飞。")
        case "speed" | "down" | "up":
            try:
                speed = int(command_list[1])
            except ValueError:
                print("警告：无法识别的非法指令序列，请重新输入。")
                continue
            print(f"执行：{command_list[0]}，目标参数：{command_list[1]}。")
        case "move":
            try:
                speed = int(command_list[2])
            except ValueError:
                print("警告：无法识别的非法指令序列，请重新输入。")
                continue
            print(f"航向修正：向{command_list[1]}移动{command_list[2]}米。")
        case "land":
            print("系统：正在自动寻迹降落。")
            break
        case _:
            print("警告：无法识别的非法指令序列，请重新输入。")

"""

"""
交互式状态机模拟：编写一个程序模拟一个简易的自动柜员机登录流程。
程序有三个状态：输入账号、输入密码、登录成功。
其中密码总共6位，用户只记得前5位是26583。最后一位使用随机数，当用户输入的6位密码和“26583”+随机数一致时，则密码正确。
用户有5次输入机会，如果超过5次则利用break强制退出程序。
示例：
请输入账号：zhangsan
请输入密码：265831
抱歉！登录失败[密码不正确]，还剩4次机会。
"""
"""
import random
root = input("请输入账号：")
password = "26583" + str(random.randint(1, 9))
i = 0
check = False
print(password)
while i < 5:
    password_input = input("请输入密码：")
    if password == password_input:
        print("密码正确")
        break
    else:
        print(f"抱歉！登录失败[密码不正确]，还剩{4-i}次机会。")
        if (4 - i) == 0:
            break
    i += 1
"""