
import uvicorn
from fastapi import FastAPI
from starlette.requests import Request
from starlette.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="htmls")

data = {
    "name": "姓名:lcalgjagjc",
    "age": "年龄:18岁",
    "height": "身高:180cm" }

@app.get("/")
def root(request: Request):
    return (templates
            .TemplateResponse("index.html", {"request": request, "data": data}))

@app.get("/items/{item_id}")
def read_item(item_id: int,item_name:str = "None"):
    return {"item_id": item_id , "item_name": item_name }

@app.get("/employees/{dept_id}/list/{status}")
def employee_info3(
        dept_id: int,
        status: str = "in",
        offset: int = 0,
        limit: int = 10,
        order_by_birthday: bool =  None):
    return {"部门ID": dept_id, "在职|离职状态": status, "跳过条数": offset, "返回条数": limit, "按生日排序": order_by_birthday}



if __name__ == '__main__':
    uvicorn.run("main:app",
                host="0.0.0.0",
                port=80,
                reload=True
                )