from typing import List

import uvicorn
from fastapi import FastAPI, Form
from starlette.requests import Request
from starlette.templating import Jinja2Templates
from starlette.responses import RedirectResponse

from model import Base, Question
from question_repositories import QuestionRepository
from question_server import QuestionServer
from question_module import QuestionModel
from session import engine

app = FastAPI()

Base.metadata.create_all(engine)

templates = Jinja2Templates(directory="htmls")

@app.get("/")
def root(request: Request, page: int = 1, search: str = ""):
    question_server = QuestionServer()
    page_size = 5
    
    if search:
        questions, total = question_server.search(search, page, page_size)
    else:
        questions, total = question_server.get_paginated(page, page_size)
    
    total_pages = (total + page_size - 1) // page_size if total > 0 else 1

    return (templates
            .TemplateResponse("main.html", {
                "request": request,
                "questions": list(questions),
                "page": page,
                "total_pages": total_pages,
                "page_size": page_size,
                "total": total,
                "search": search
            }))

@app.get("/add")
def add_question_page(request: Request):
    return templates.TemplateResponse("add_question.html", {"request": request})

@app.post("/add")
def add_question(
    title: str = Form(...),
    content: str = Form(...),
    answer: str = Form(...),
    level: str = Form(...),
    type: str = Form(...),
    tags: str = Form(...),
    score: int = Form(...)
):
    question_server = QuestionServer()
    question = QuestionModel(
        title=title,
        content=content,
        answer=answer,
        level=level,
        type=type,
        tags=tags,
        score=score
    )
    question_server.save(question)
    return RedirectResponse(url="/", status_code=303)

@app.get("/delete/{question_id}")
def delete_question(question_id: int):
    question_server = QuestionServer()
    question_server.delete(question_id)
    return RedirectResponse(url="/", status_code=303)

if __name__ == '__main__':

    uvicorn.run("main:app",
                host="0.0.0.0",
                port=80,
                reload=True
                )