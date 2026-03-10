from starlette.middleware.cors import CORSMiddleware

from core.exception_handlers import register_exception_handlers
# 初始化日志配置
from core.settings import setup_logging
setup_logging()

from fastapi import FastAPI

from core.settings import config
from api.admin_api import router as admin_router
from api.category_api import router as category_router
from api.project_api import router as project_router

app = FastAPI(
    title = config.PROJECT_NAME,
    description = "项目接口",
    version = "0.1.0"
)

# 异常处理
register_exception_handlers(app)


# 解决跨域：添加 CORS 中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有源（生产环境不推荐！）
    allow_credentials = True,
    allow_methods=["*"],  # 允许所有方法
    allow_headers=["*"],  # 允许所有请求头
)

# 路由
app.include_router(admin_router,  prefix = "/api/v1/admin")
app.include_router(category_router,  prefix = "/api/v1/category")
app.include_router(project_router,  prefix = "/api/v1/project")


@app.get("/")
def index():
    return {"message": "欢迎使用项目接口"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host = config.HOST, port = config.PORT, reload = config.RELOAD)