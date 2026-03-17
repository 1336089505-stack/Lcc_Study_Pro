"""
2.	编写一个FastAPI路径操作函数，使用GET方法，
路径为 /calculate。该函数接收两个查询参数 a 和 b，
均为浮点数类型，并返回它们的和（以JSON格式，例如 {"sum": 3.5}）。
要求 a 和 b 都是必填参数。
"""
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

@app.get("/calculate")
def func(a:float,b:float):
    return {"sum":a+b}
#http://127.0.0.1/calculate?a=1.1&b=2.1

if __name__ == '__main__':
    uvicorn.run("program2:app", host='127.0.0.1', port= 80, reload=True)
