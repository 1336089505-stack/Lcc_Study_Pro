"""
4.	编写一个FastAPI路径操作函数，使用POST方法，路径为 /items。
函数接收一个JSON请求体，该请求体应包含字段 name（字符串）和 price（浮点数）。
要求使用Pydantic模型定义请求体的结构。函数返回一个JSON对象，
内容为接收到的数据，并额外添加一个字段 create_at 为当前时间戳（可使用 time.time()）。
"""
from pydantic import BaseModel
from fastapi import FastAPI
import time
import uvicorn

app = FastAPI(
    title = 'fastapi',
    description = "接口",
    version = "0.1.0"
)
class Request(BaseModel):
    name: str
    price: float

@app.get("/")
def welcome():
    return {"message": "Hello"}

@app.post("/items")
def func(item:Request):
    result = {"name":item.name,"price":item.price,"create_at":time.time()}
    return result


if __name__ == '__main__':
    uvicorn.run("program4:app", host='127.0.0.1', port= 80, reload=True)