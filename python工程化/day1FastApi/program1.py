"""
1.	编写一个FastAPI路径操作函数，使用GET方法，
路径为 /greet/{name}。函数接收路径参数 name（字符串类型），
并返回一个JSON对象 {"message": "Hello, {name}"}，其中 {name} 为传入的实际值。
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

@app.get("/greet/{name}")
def func(name: str):
    return {"message": f"Hello, {name}"}
#http://127.0.0.1/greet/lcc

if __name__ == '__main__':
    uvicorn.run("program1:app", host='127.0.0.1', port= 80, reload=True)
