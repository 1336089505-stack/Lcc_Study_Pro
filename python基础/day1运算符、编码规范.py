"""
编写购物车价格计算程序：
1.	提示用户输入商品单价和购买数量
2.	接收用户输入后，判断是否为正确的值，如整数、浮点数
3. 计算总价（单价 × 数量）
4. 使用if语句判断总价是否超过100元，如果超过则打9折。
5. 输出原始总价和折后价格（如果打折）
6. 要求使用字符串格式化显示金额（保留2位小数）

示例：
请输入单价：25.5元
输出：抱歉，您输入的单价不是完整的数字
程序结束

请输入单价：25.5
请输入数量：4
输出：原始总价：102.00元，折后价格：91.80元
程序结束
"""

"""
price_input = input("请输入单价：")
try:
    price = float(price_input)
except ValueError:
    print("抱歉，您输入的单价不是完整的数字")
    exit()

quantity_input = input("请输入数量：")
try:
    quantity = int(quantity_input)
except ValueError:
    print("抱歉，您输入的数量不是完整的数字")
    exit()


total = price * quantity
if total > 100:
    discount_total = total * 0.9
    print(f"原始总价：{total:.2f}元，折后价格：{discount_total:.2f}元")
else:
    print(f"原始总价：{total:.2f}元，无需打折")
"""


"""
编写温度单位转换程序：
1. 提示用户输入温度值和单位（C表示摄氏度，F表示华氏度）
2. 如果输入的是摄氏度，转换为华氏度：F = C × 9/5 + 32
3. 如果输入的是华氏度，转换为摄氏度：C = (F - 32) × 5/9
4. 使用if语句判断转换方向
5. 输出转换结果，保留1位小数
6. 要求处理大小写输入（如'c'和'C'都应该识别）

示例：
输入：25 C
输出：25.0摄氏度 = 77.0华氏度

输入：77 F  
输出：77.0华氏度 = 25.0摄氏度
"""
parts_input = input("输入温度值和单位:")
parts = parts_input.split(" ")
print(parts)
if (parts[1] == "F") | (parts[1] == "f"):
    print("%.1f华氏度 = %.1f摄氏度"%(float(parts[0]), (float(parts[0])- 32)*5/9 ))
elif (parts[1] == "C") | (parts[1] == "c"):
    print("%.1f摄氏度 = %.1f华氏度" % (float(parts[0]), float(parts[0]) * 9 / 5 + 32))





