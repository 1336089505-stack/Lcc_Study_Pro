import uvicorn
from fastapi import FastAPI
from starlette.requests import Request
from starlette.templating import Jinja2Templates

from text2.newsdao import get_news, get_by_id
from text2.user import User

app = FastAPI()

templates = Jinja2Templates(directory="htmls")

@app.get("/")
async def new_list(request: Request):
    news = get_news()

    return templates.TemplateResponse("new_list.html", {"request": request, "news": news})

@app.get("/details/{id}")
async def details(request: Request, id: int):

    new = get_by_id(id)

    return templates.TemplateResponse("details.html", {"request": request, "new": new})


@app.post("/new1")
def news(ems: dict):
    print(ems)
    return ems

@app.post("/new2")
def news2(ems: User):
    print(ems)
    return ems

if __name__ == '__main__':
    uvicorn.run("main:app",
                host="0.0.0.0",
                port=8000,
                reload=True
                )
