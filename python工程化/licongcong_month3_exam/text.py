from repositories.product_repositories import ProductRepository
from repositories.deliveryman_repositories import DeliverymanRepository
from repositories.order_info_repositories import OrderInfoRepository
from model import Deliveryman, OrderInfo, Product
from session import get_session

if __name__ == '__main__':
    with get_session() as session:
        products = ProductRepository(session)

        #添加
        product_list = [
            Product(name="红富士苹果", price=890, stock=120),
            Product(name="山东大樱桃", price=3980, stock=80),
            Product(name="泰国金枕榴莲", price=5990, stock=35),
            Product(name="阳光玫瑰葡萄", price=2580, stock=60),
            Product(name="丹东99草莓", price=4280, stock=100),
            Product(name="秘鲁蓝莓", price=1280, stock=150),
            Product(name="新疆阿克苏苹果", price=650, stock=200),
            Product(name="福建琯溪蜜柚", price=350, stock=180),
            Product(name="四川丑橘不知火", price=780, stock=160),
            Product(name="海南麒麟西瓜", price=520, stock=90),
            Product(name="云南高山沃柑", price=680, stock=220),
            Product(name="智利车厘子", price=5680, stock=70),
            Product(name="广西砂糖橘", price=450, stock=300),
            Product(name="陕西洛川苹果", price=580, stock=250),
            Product(name="广东增城荔枝", price=2880, stock=110),
            Product(name="浙江仙居杨梅", price=3680, stock=85),
            Product(name="河北皇冠梨", price=320, stock=240),
            Product(name="湖北秭归脐橙", price=550, stock=210),
            Product(name="甘肃花牛苹果", price=620, stock=190),
            Product(name="山西运城冬枣", price=980, stock=130)
        ]
        products.get_all_products(product_list)

