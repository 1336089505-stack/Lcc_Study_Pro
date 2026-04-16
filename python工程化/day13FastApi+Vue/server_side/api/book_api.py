from fastapi import APIRouter, Path, Body

from schema.schema_module import BookModel, BookRequest
from service.book_service import BookService
from core.response import ApiResponse

router = APIRouter(tags=["书籍模块"])


@router.get("/api/books/home", response_model=ApiResponse, description="获取某分类下详情列表")
def get_all():
    service = BookService()
    result = service.get_all()
    return ApiResponse(code=200, message="获取所有书籍", data=result)


@router.get("/api/books/bookDetail", response_model=ApiResponse, description="获取某分类下详情列表")
def get_book(id:int):
    service = BookService()
    result = service.get(id)
    return ApiResponse(code=200, message="获取所有书籍", data=result)


@router.post("/api/books/add_book", response_model=ApiResponse[BookModel], summary="新增单本书籍")
def add_book(book_in: BookModel):
    service = BookService()
    result = service.save(book_in)
    return ApiResponse(code=200, message="新增成功", data=result)


@router.post("/api/books/update_book", response_model=ApiResponse[BookModel], summary="修改单本书籍")
def update_book(book_in: BookModel):
    service = BookService()
    service.update(book_in)
    return ApiResponse(code=200, message="修改成功", data=book_in)

@router.post("/api/books/delete_book", response_model=ApiResponse, description="删除书籍")
def delete_book(req: BookRequest):
    service = BookService()
    service.delete(req.id)
    return ApiResponse(code=200, message="删除成功", data={})
