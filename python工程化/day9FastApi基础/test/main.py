import uvicorn
from fastapi import FastAPI
from starlette.requests import Request
from starlette.templating import Jinja2Templates

#首页 》 新闻列表 》 新闻详情 》新闻列表

app = FastAPI()

#加载模板
templates = Jinja2Templates(directory="htmls")

#处理请求

#首页
@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/new_list")
def new_list(request: Request):
    news = [
        {"id": 1, "title": "台湾掀起“抢塑潮” 国台办回应"},
        {"id": 2, "title": "4月1日起一批国家标准正式实施"},
        {"id": 3, "title": "旅游新规落地 将带来哪些新变化"},
        {"id": 4, "title": "王伟牺牲25年 妻子:这盛世如你所愿"},
        {"id": 5, "title": "县委书记用6秒搞定足球赛闭幕式"}
    ]
    return templates.TemplateResponse("new_list.html", {"request": request,
                                                        "news": news})
@app.get("/new_list/{id}")
def details(id: int,request: Request):
    contexts = {
        1:{"title":"台湾掀起“抢塑潮” 国台办回应", "context":"4月1日，国台办发言人张晗回应“台湾近期因中东战事掀起的‘抢塑潮’”。她表示，和平统一后，两岸实现互联互通、应通尽通。无论外部形势如何动荡不安，都可以为台湾的能源资源安全、工业生产物资供给提供及时保障，台湾同胞再也无需为各种能源、物资短缺而焦虑。‌"},
        2:{"title":"4月1日起一批国家标准正式实施", "context":"4月1日起，一批国家标准开始实施，将为引领和规范新兴产业及未来产业的发展、推动传统产业升级、提升交通运输和游览服务质量、保护消费者权益等提供标准支撑"},
        3:{"title":"旅游新规落地 将带来哪些新变化", "context":"新版《旅游规划通则》4月1日起实施。景区客流调控更准，游览节奏更从容；地方特色得到挖掘，每站各有韵味；标识导览等标准清晰，出行体验更顺心。游客意见也可参与规划，让每次出发都有新的遇见"},
        4:{"title":"王伟牺牲25年 妻子:这盛世如你所愿", "context":"25年前的4月1日，海军航空兵飞行员王伟在南海拦截美军侦察机时壮烈牺牲，终年33岁。近日，妻子阮国琴深情表示：“当年你总说，咱们的飞机落后，如今，咱们的歼-20已经翱翔蓝天、山东舰的甲板上停满了‘飞鲨’……阿伟，你看到了吗？这盛世如你所愿。”‌"},
        5:{"title":"县委书记用6秒搞定足球赛闭幕式", "context":"近日，黔东南“州长杯”榕江赛区闭幕式，县委书记仅用“闭幕”两字完成发言，全程耗时6秒。网友：我还没反应过来就结束了。‌"}
    }
    # 根据传入的id，获取对应的title和context
    new = contexts[id]
    return templates.TemplateResponse("details.html", {"request": request,"new":new})

if __name__ == '__main__':
    uvicorn.run("main:app",
                host="0.0.0.0",
                port=80,
                reload=True
                )