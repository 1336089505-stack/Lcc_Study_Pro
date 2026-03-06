"""
1.	模块封装与导入
编写一个名为 calculator 的模块，
在其中定义四个函数：add(x, y), subtract(x, y), multiply(x, y), divide(x, y)，
分别实现加、减、乘、除运算。除法函数需处理除数为零的情况，抛出 ValueError 异常。
然后，编写一个主程序 main.py，导入该模块并测试所有函数，使用 try-except 处理除法异常。
"""
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        raise ValueError("divide by zero")
    else:
        return x / y

