"""
5.	模块的缓存与重载
编写一个模块 counter.py，其中定义了一个全局变量 count = 0 和一个函数 increment()，
该函数将 count 加1并打印当前值。编写主程序 reload_test.py：
o	导入 counter 模块，调用几次 increment()。
o	使用 importlib.reload() 重载 counter 模块。
o	再次调用 increment()。
o	观察并解释输出结果。思考：如何能“重置”计数器？尝试从 sys.modules 中删除 counter 后再导入。
"""
count = 0
def increment():
    global count
    count += 1
    print(count)