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

import json
class Config:
    config = None

    @staticmethod
    def get_config():
        if Config.config is None:
            with open("config.json", "r") as f:
                print("读取config文件")
                Config.config = json.load(f)
        return Config.config







