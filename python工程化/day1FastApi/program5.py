"""
5.	编写一个FastAPI路径操作函数，使用GET方法，路径为 /files/{file_path:path}。
该函数接收一个路径参数 file_path，它本身是一个路径（如 docs/images/photo.jpg）。
函数应返回一个JSON，包含原始的文件路径字符串以及该路径的父目录（可以使用 os.path.dirname 获取）。
例如请求 /files/home/user/data.txt
返回 {"full_path": "home/user/data.txt", "parent": "home/user"}。
注意处理路径分隔符的统一。
"""
import os
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

@app.get("/files/{file_path:path}")
def func(file_path:str):
    parent_dir = os.path.dirname(file_path)
    return {
        "full_path": file_path,
        "parent": parent_dir
    }


if __name__ == '__main__':
    uvicorn.run("program5:app", host='127.0.0.1', port= 80, reload=True)