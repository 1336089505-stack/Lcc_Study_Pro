"""
6.	编写一个FastAPI路径操作函数，使用GET方法，路径为 /validate/{number}。
函数接收路径参数 number，要求必须是正整数（大于0的整数）。
如果参数验证失败，FastAPI应自动返回422错误；
如果验证成功，则返回 {"number": number, "is_even": True/False} 指示该数是否为偶数。
请通过类型标注和可能的额外校验实现此功能。
"""
from fastapi import FastAPI
from pydantic import PositiveInt
import uvicorn

app = FastAPI(
    title = 'fastapi',
    description = "接口",
    version = "0.1.0"
)

@app.get("/")
def welcome():
    return {"message": "Hello"}

@app.get("/validate/{number}")
def func(number:PositiveInt):
    is_even = number % 2 == 0
    return {
        "number": number,
        "is_even": is_even
    }

if __name__ == '__main__':
    uvicorn.run("program6:app", host='127.0.0.1', port= 80, reload=True)