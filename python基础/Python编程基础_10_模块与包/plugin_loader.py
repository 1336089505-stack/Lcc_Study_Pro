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
import importlib
import os
from types import ModuleType

data = {'input':'test'}
module_list:list[ModuleType] = []
for filename in os.listdir("plugins/"):
    if filename[0] != "_":
        print(filename)
        filename_tmp = filename.replace(".py", "")
        module_list.append(importlib.import_module( "."+filename_tmp,"plugins"))
for module in module_list:
    print(module.execute(data))





