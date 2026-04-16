from starlette.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from core.settings import config
from api.book_api import router as book_router

app = FastAPI(
    title = config.PROJECT_NAME,
    description = "项目接口",
    version = "0.1.0"
)

# 解决跨域：添加 CORS 中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有源（生产环境不推荐！）
    allow_credentials = True,
    allow_methods=["*"],  # 允许所有方法
    allow_headers=["*"],  # 允许所有请求头
)

# 路由
app.include_router(book_router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host = config.HOST,
                port = config.PORT, reload = config.RELOAD)