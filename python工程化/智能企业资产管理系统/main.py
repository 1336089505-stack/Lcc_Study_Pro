from fastapi import FastAPI
from api.v1 import department_api, user_api  # 导入你的API

app = FastAPI(title="资产管理系统", version="1.0.0")

# 注册路由
app.include_router(department_api.router)


@app.get("/")
def health_check():
    return {"status": "ok", "msg": "系统运行正常"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)