from fastapi import FastAPI,Request
from starlette.responses import JSONResponse

from core.exceptions import QiDianAiException
from core.status_code import StatusCodes
from core.qidian_response import fail



def register_exception_handlers(app: FastAPI):

    @app.exception_handler(QiDianAiException)
    async def qi_dian_ai_exception_handler(request: Request, exception: QiDianAiException):

        return JSONResponse(
            status_code = 500,
            content = fail(status_code = exception.get_status_code(), message = exception.message).model_dump() #-->fail()->ApiResponse
        )

    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc: Exception):
        return JSONResponse(
            status_code = 500,
            content = fail(status_code = StatusCodes.SYSTEM_ERROR, message = "系统内部错误").model_dump()
        )