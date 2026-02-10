import time

if __name__ == '__main__':
    """
    1.	模块封装与导入
    编写一个名为 calculator 的模块，
    在其中定义四个函数：add(x, y), subtract(x, y), multiply(x, y), divide(x, y)，
    分别实现加、减、乘、除运算。除法函数需处理除数为零的情况，抛出 ValueError 异常。
    然后，编写一个主程序 main.py，导入该模块并测试所有函数，使用 try-except 处理除法异常。
    """
    import calculator
    calculator.add(5,2)
    calculator.subtract(5,2)
    calculator.multiply(5,2)
    try:
        calculator.divide(5,2)
    except ValueError as e:
        print(e)

    """
    2.	包的组织与 __init__.py
    创建一个包 shapelib，包含两个子模块 circle 和 rectangle。
    o	在 circle.py 中定义函数 area(radius) 和 circumference(radius)。
    o	在 rectangle.py 中定义函数 area(length, width) 和 perimeter(length, width)。
    o	在 shapelib 的 __init__.py 中，编写代码，使得当用户使用 from shapelib import * 时，
    只能导入两个面积函数（即 circle.area 和 rectangle.area），
    并分别为它们起别名 circle_area 和 rect_area。
    同时，允许用户通过 import shapelib 后使用 shapelib.circle.circumference 的方式访问周长函数。
    编写一个测试脚本，演示这两种导入方式的使用。
    """
    from shapelib import *
    circle_area(1)
    rect_area(3,5)

    import shapelib
    shapelib.circle.circumference(2)

    """
    3.	动态导入与插件架构
    编写一个主程序 plugin_loader.py。
    假设在 plugins/ 目录下有多个插件模块（如 plugin_a.py, plugin_b.py），
    每个插件模块中都定义了一个同名的函数 execute(data)。主程序需要：
    o	动态发现 plugins/ 目录下所有 .py 文件（排除 __init__.py 和以 _ 开头的文件）。
    o	动态导入这些模块。
    o	准备一个字典 data，例如 {‘input‘: ‘test‘}。
    o	按顺序调用每个插件的 execute 函数，并将 data 字典传递给它们。
    （提示：使用 os.listdir, importlib.import_module）
    """

    """
    4.	模块配置与单例模式
    编写一个配置管理模块 config.py。要求：
    o	模块首次导入时，从一个名为 config.json 的 JSON 文件中加载配置
    （例如包含 {‘host‘: ‘localhost‘, ‘port‘: 8080}）。
    o	在模块中提供一个函数 get_config()，它返回配置字典。
    o	确保配置只从文件加载一次，即使模块被多次导入或重载。
    o	在主程序中导入 config 模块，调用 get_config() 并打印配置。
    修改 config.json 文件的内容，尝试在程序中重新获取配置，观察行为（需要用到 importlib.reload）。
    """
    import importlib
    import config

    start_time = time.time()  # 记录开始时间
    print("计时器已启动（按 Ctrl+C 停止）...")
    try:
        while True:  # 无限循环
            # 计算已流逝时间（保留1位小数）
            elapsed_time = round(time.time() - start_time, 1)
            importlib.reload(config)
            print(config.Config.get_config())# 覆盖当前行打印（避免刷屏）
            time.sleep(1)  # 每0.1秒更新一次
    except KeyboardInterrupt:
        # 捕获 Ctrl+C，优雅退出
        print("\n计时器已停止")


    """
    5.	模块的缓存与重载
    编写一个模块 counter.py，其中定义了一个全局变量 count = 0 和一个函数 increment()，
    该函数将 count 加1并打印当前值。编写主程序 reload_test.py：
    o	导入 counter 模块，调用几次 increment()。
    o	使用 importlib.reload() 重载 counter 模块。
    o	再次调用 increment()。
    o	观察并解释输出结果。思考：如何能“重置”计数器？尝试从 sys.modules 中删除 counter 后再导入。
    """
