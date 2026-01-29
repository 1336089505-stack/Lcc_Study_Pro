"""
编写一个程序，实现以下功能：
从用户输入接收一个包含整数的列表（如：输入"1 3 2 4 2 3 1"）
去除列表中的重复元素
对结果进行升序排序
输出处理后的列表
要求：不能使用set()函数去重，要手动实现去重逻辑。
"""
from os.path import join

"""
num_input_t = input("输入一个包含整数的列表：")
num_input = num_input_t.split()
num_list_tmp = [int(i) for i in num_input]
num_list =[]
for i in num_list_tmp:
    if i not in num_list:
        num_list.append(i)
num_list.sort()
print(num_list)
"""
"""
编写一个程序，分析一段文本的统计信息：
接收用户输入的一段英文文本
统计并输出：总字符数、字母数、数字数、空格数、单词数
找出文本中出现频率最高的3个字符（不区分大小写）
将文本中的所有单词转换为首字母大写形式
示例输入："hello world! This is a test. 123"
示例输出要求格式整齐清晰。
"""
"""
eng_str = "hello world! This is a test. 123"
print("总字符数:",len(eng_str))
space_num,eng_num,math_num,word_num= 0,0,0,0
word_tmp = eng_str.split()
for ch in eng_str:
    if ord(ch) == 32:
        space_num += 1
    elif 48 <= ord(ch) <= 57:
        math_num += 1
    elif 65 <= ord(ch) <= 90 or 97 <= ord(ch) <= 122:
        eng_num += 1
for ch in word_tmp:
    if 65 <= ord(ch[0]) <= 90 or 97 <= ord(ch[0]) <= 122:
        word_num += 1
print("字母数:",eng_num)
print("数字数:",math_num)
print("空格数:",space_num)
print("单词数:",word_num)

eng_str_tmp = eng_str.lower()
ch_all_count= {}
for ch in eng_str_tmp:
    ch_all_count[ch] = ch_all_count.get(ch, 0) + 1
sorted_desc = sorted(ch_all_count.items(), key=lambda x: x[1], reverse=True)
print("出现频率最高的3个字符：", sorted_desc[:3])
print("所有单词转换为首字母大写形式：", eng_str_tmp.title())
"""

"""
将列表或字符串中的元素进行反转。
示例：
输入：5,2,7,9,3,1,6
输出：6,1,3,9,7,2,5
输入：中华人民共和国
输出：国和共民人华中
"""
"""
list_num_input = input("输入元素:")
list_num = list_num_input.split()
list_tmp = []
for ch in list_num:
    list_tmp.insert(0,ch)
print(list_tmp)
"""

"""
编写一个程序，实现以下功能：
1.	创建一个空列表 numbers。
2.	使用 while 循环，让用户重复输入整数，直到用户输入小于0的值时停止。
3.	将用户输入的数字（除了-1）添加到列表 numbers 中。
4.	循环结束后，计算并打印该列表所有元素的平均值（保留两位小数）。
示例：
输入： 10, 20, 30, -1
输出： 平均值为: 20.00
"""
"""
numbers_list = []
while True:
    num = int(input('输入整数:'))
    if num < 0 :
        break
    numbers_list.append(num)

sum_num = 0
for num in numbers_list:
    sum_num += num

num_average = sum_num / len(numbers_list)
print("平均值为: %.2f"%num_average)
"""

