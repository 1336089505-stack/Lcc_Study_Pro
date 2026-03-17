"""
3.	使用Python的枚举类型，定义一个名为 Color 的枚举类，
包含三个成员：RED、GREEN、BLUE。然后编写一个FastAPI路径操作函数，
使用GET方法，路径为 /color/{color_name}。
函数接收路径参数 color_name，类型为 Color 枚举。
函数返回一个JSON对象，包含所选颜色的名称和对应的值（例如 {"name": "RED", "value": "red"}，
假定枚举值设置为字符串 "red"、"green"、"blue"）。
"""
from enum import Enum

from fastapi import FastAPI
import uvicorn

app = FastAPI(
    title = 'fastapi',
    description = "接口",
    version = "0.1.0"
)
@app.get("/")
def welcome():
    return {"message": "Hello"}

class Color(str, Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"

@app.get("/color/{color_name}")
def func(color_name:Color):
    return {"name": color_name.name, "value": color_name.value}
#http://127.0.0.1/color/green

if __name__ == '__main__':
    uvicorn.run("program3:app", host='127.0.0.1', port= 80, reload=True)
