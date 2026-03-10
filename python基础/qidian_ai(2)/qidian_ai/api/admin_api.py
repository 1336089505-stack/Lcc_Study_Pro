from fastapi import APIRouter

router = APIRouter(tags = ["后台"]) # = "后台管理系统接口"

@router.get("/", description="获取后台信息")
def home():
    return "后台管理系统"
