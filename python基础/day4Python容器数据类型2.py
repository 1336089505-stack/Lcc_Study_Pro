"""
编写一个程序，实现以下功能：
1.	已知两个列表：list1=[1,2,3,4,5,6], list2=[4,5,6,7,8]。
2.	找出 既在list1中也存在，又在list2中也存在 的元素，放入一个新列表 common_list。
3.	找出 在list1中存在，但不在list2中存在 的元素，放入一个新列表 only_in_list1。
4.	打印两个新列表。
示例输出：
共有的元素:[4,5,6]
仅在list1中的元素:[1,2,3]
"""

"""
list1=[1,2,3,4,5,6]
list2=[4,5,6,7,8]
common_list = []
only_in_list1=[]
for num1 in list1:
    check = False
    for num2 in list2:
        if num1 == num2:
            common_list.append(num1)
            check = True
    if not check:
        only_in_list1.append(num1)
print("共有的元素:",common_list)
print("仅在list1中的元素:",only_in_list1)
"""

"""
编写程序实现集合的基本运算：预定义两个集合：set1 = {1, 2, 3, 4, 5}，set2 = {4, 5, 6, 7, 8}，
计算并输出以下结果：
1.	并集（两个集合的所有元素）
2.	交集（两个集合的共同元素）
3.	差集（在set1中但不在set2中的元素）
4.	对称差集（只在一个集合中出现的元素）
判断并输出以下关系：
1.	set1是否是set2的子集
2.	set2是否是set1的超集
3.	两个集合是否有交集
将运算结果用可视化方式展示（使用字符表示元素是否存在）
"""

"""
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("并集",set1 | set2)
print("交集",set1 & set2)
print("差集",set1 - set2)
print("对称差集",set1.symmetric_difference(set2))
print("set1是否是set2的子集",set1.issubset(set2))
print("set2是否是set1的子集",set1.issubset(set2))
print("两个集合是否有交集",set1.isdisjoint(set2))
"""

"""
编写程序统计一段文本中单词的出现频率：
给定文本：text = "apple banana apple orange banana apple grape orange apple"
实现以下功能：
1. 	将文本分割成单词列表
2. 	使用字典统计每个单词出现的次数
3. 	找出出现次数最多的单词
4. 	计算总共的单词数和不重复单词数
5. 	按单词出现次数从高到低排序输出
6. 	统计每个单词占总数的百分比
输出格式要求整齐，使用制表符对齐
"""

"""
text = "apple banana apple orange banana apple grape orange apple"
words_list = text.split()
print("----单词列表----")
print(words_list)
words_count= {}
for word in words_list:
    words_count[word] = words_count.get(word, 0) + 1
print("----字典统计每个单词出现的次数----")
print(words_count)
words_list_sorted = sorted(words_count.items(), key=lambda x: x[1], reverse=True)
print("----出现次数最多的单词----")
print(words_list_sorted[:1])
print("----总共的单词数----")
all_count = 0
for v in words_count:
    all_count+= words_count[v]
print(all_count)
print("----不重复单词数----")
no_all_count = 0
for v in words_count:
    no_all_count+= 1
print(no_all_count)
print("----单词出现次数从高到低排序----")
print(words_list_sorted)
print("----统计每个单词占总数的百分比----")
for v in words_count:
    words_count[v] =  f"{(words_count[v]/ all_count*100):.2f}%"
print(words_count)
"""

"""
创建一个简单的联系人管理系统：
初始化一个嵌套字典存储联系人信息：
contacts = {
"张三": {"phone": "13800138000", "email": "zhangsan@email.com", "group": "朋友"},
"李四": {"phone": "13900139000", "email": "lisi@email.com", "group": "同事"},
"王五": {"phone": "13700137000", "email": "wangwu@email.com", "group": "家人"}
}
实现以下操作：
1. 	添加新联系人："赵六"，电话"13600136000"，邮箱"zhaoliu@email.com"，分组"同学"
2. 	修改"李四"的电话为"13900139111"
3. 	查询"张三"的所有信息
4. 	按分组统计联系人数量
5. 	找出所有邮箱包含"@email.com"的联系人
6. 	遍历并格式化输出所有联系人信息
7. 	实现简单的搜索功能（按姓名部分匹配）
"""
contacts = {
"张三": {"phone": "13800138000", "email": "zhangsan@email.com", "group": "朋友"},
"李四": {"phone": "13900139000", "email": "lisi@email.com", "group": "同事"},
"王五": {"phone": "13700137000", "email": "wangwu@email.com", "group": "家人"}
}
contacts_tmp = {"赵六": {"phone": "13600136000", "email": "zhaoliu@email.com", "group": "同学"}}
contacts.update(contacts_tmp)
print(contacts)

contacts["李四"]["phone"]= "13900139111"
print(contacts)

print(contacts["张三"])

contacts_count= {}
for word in contacts:
    contacts_count[contacts[word]["group"]] = "联系人数：%d"%(contacts.get(contacts[word]["group"], 0) + 1)
print(contacts_count)

contacts_emile= {}
for word in contacts:
    list_tmp = str(contacts[word]["email"]).split("@")
    if list_tmp[1] == "email.com":
        contacts_emile[word] = contacts[word]["email"]
print(contacts_emile)

for key in contacts:
    print("---联系人信息---")
    print("姓名：",key)
    for k in contacts[key]:
        print(k,":",contacts[key][k])

name = input("输入查找的姓名：")
for key in contacts:
    if key == name:
        print(f"---{name}信息---")
        for k in contacts[key]:
            print(k, ":", contacts[key][k])