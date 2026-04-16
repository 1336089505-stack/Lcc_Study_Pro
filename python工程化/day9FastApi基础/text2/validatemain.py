from datetime import date
from typing import Annotated

import uvicorn
from fastapi import FastAPI, Query
from starlette.requests import Request
from starlette.templating import Jinja2Templates

from text2.newsdao import get_news, get_by_id
from text2.user import User

app = FastAPI()

templates = Jinja2Templates(directory="htmls")


@app.get("/search_employee", description="员工搜索接口", tags=["员工模块"])
def search_employee(
        name: Annotated[
            str,
            Query(max_length=10, description="按员工姓名搜索", examples=["张三", "李四"])
        ] = None,

        birthday: Annotated[
            date,
            Query( lt = date(2008, 1, 1), description="按员工生日搜索, 格式：YYYY-MM-DD", example="2020-11-05")
        ] = None,

        salary: Annotated[
            float,
            Query(gt=0, lt=100000, description="按员工薪资搜索", example=5000.00)
        ] = None,
):
    return {"name": name, "birthday": birthday, "salary": salary}


if __name__ == '__main__':
    uvicorn.run("validatemain:app",
                host="0.0.0.0",
                port=8000,
                reload=True
                )
