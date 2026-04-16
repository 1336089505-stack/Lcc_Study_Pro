from session import get_session,engine
from repositories.product_repositories import ProductRepository
from repositories.deliveryman_repositories import DeliverymanRepository
from repositories.order_info_repositories import OrderInfoRepository
from model import Deliveryman, OrderInfo, Product,Base
from session import get_session

def add_products():
    """
    添加商品
    :return:
    """
    while True:
        product_name = input("请输入输入商品名称:")
        product_price = float(input("请输入输入商品单价:"))
        product_stock = int(input("请输入输入商品初始库存:"))
        product_list = [Product(
            name=product_name,
            price=product_price,
            stock=product_stock
        )]
        with get_session() as session:
            products = ProductRepository(session)
            state = products.get_all_products(product_list)
            print(state)
        continue_add = input("是否继续添加？Y/N:")
        if continue_add == "N" or continue_add == "n":
            break

def find_products():
    """
    查询商品
    :return:
    """
    while True:
        print("----------------------- 查找商品 -----------------------")
        print("-------------------- 1.商品名称查找 --------------------")
        print("-------------------- 2.商品ID查找 ---------------------")
        print("-------------------- 3.所有商品查找 --------------------")
        menu_num = int(input("请输入编号选择："))
        match menu_num:
            case 1:
                product_name = input("请输入输入商品名称:")
                with get_session() as session:
                    products = ProductRepository(session)
                    results = products.find_by_id_or_name_and_all_product(p_name = product_name)
                    for result in results:
                        print(result)
            case 2:
                product_id = int(input("请输入输入商品ID:"))
                with get_session() as session:
                    products = ProductRepository(session)
                    results = products.find_by_id_or_name_and_all_product(p_id=product_id)
                    for result in results:
                        print(result)
            case 3:
                with get_session() as session:
                    products = ProductRepository(session)
                    results = products.find_by_id_or_name_and_all_product()
                    for result in results[0]:
                        print(result)
                    for flag in results[1]:
                        print("库存不足5公斤：",flag)

        continue_find = input("是否继续查找？Y/N:")
        if continue_find == "N" or continue_find == "n":
            break

def update_products():
    """
    修改商品
    :return:
    """
    while True:
        product_id = int(input("请输入商品ID:"))
        product_price = float(input("请输入商品单价:"))
        product_stock = int(input("请输入商品初始库存:"))
        with get_session() as session:
            products = ProductRepository(session)
            result = products.find_by_id_update_price_and_stock(
                p_id=product_id,p_stock=product_stock,p_price=product_price)
            if result:
                print("修改成功")
            else:
                print("商品不存在")
        continue_update = input("是否继续修改？Y/N:")
        if continue_update == "N" or continue_update == "n":
            break

def delete_products():
    """
    删除商品
    :return:
    """
    while True:
        product_id = int(input("请输入输入商品ID:"))
        with get_session() as session:
            products = ProductRepository(session)
            result = products.find_by_id_delete_product(p_id=product_id)
            if result == -1:
                print("商品不存在")
            elif result == -2:
                print("该商品存在关联订单，无法删除")
            else:
                print("商品删除成功")
        continue_delete = input("是否继续删除1"
                                "？Y/N:")
        if continue_delete == "N" or continue_delete == "n":
            break

def product_management():
    """
    商品管理
    :return:
    """
    while True:
        print("----------------------- 商品管理 -----------------------")
        print("---------------------- 1.添加商品 ----------------------")
        print("---------------------- 2.查找商品 ----------------------")
        print("---------------------- 3.修改商品 ----------------------")
        print("---------------------- 4.删除商品 ----------------------")
        print("--------------------- 5.返回主菜单 ---------------------")
        menu_num = int(input("请输入编号选择："))
        match menu_num:
            case 1:
                add_products()
            case 2:
                find_products()
            case 3:
                update_products()
            case 4:
                delete_products()
            case 5:
                break

def add_delivery():
    """
    添加商品
    :return:
    """
    while True:
        delivery_name = input("请输入配送员姓名:")
        delivery_phone = input("请输入配送员手机号:")
        delivery_list = [Deliveryman(
            name=delivery_name,
            phone=delivery_phone
        )]
        with get_session() as session:
            delivery = DeliverymanRepository(session)
            state = delivery.get_all_deliveryman(delivery_list)
            print(state)
        continue_add = input("是否继续添加？Y/N:")
        if continue_add == "N" or continue_add == "n":
            break


def find_delivery():
    """
    查询配送员
    :return:
    """
    while True:
        print("---------------------- 查寻配送员 ---------------------")
        print("------------------- 1.配送员名字查找 -------------------")
        print("------------------- 2.配送员ID查找 --------------------")
        print("------------------- 3.所有配送员查找 -------------------")
        menu_num = int(input("请输入编号选择："))
        match menu_num:
            case 1:
                delivery_name = input("请输入输入配送员名称:")
                with get_session() as session:
                    delivery = DeliverymanRepository(session)
                    results = delivery.find_by_id_or_name_and_all_deliveryman(p_name=delivery_name)
                    for result in results:
                        print(result)
            case 2:
                product_id = int(input("请输入输入配送员ID:"))
                with get_session() as session:
                    delivery = DeliverymanRepository(session)
                    results = delivery.find_by_id_or_name_and_all_deliveryman(p_id=product_id)
                    for result in results:
                        print(result)
            case 3:
                with get_session() as session:
                    delivery = DeliverymanRepository(session)
                    results = delivery.find_by_id_or_name_and_all_deliveryman()
                    for on_duty in results[0]:
                        print("在岗的配送员：", on_duty)
                    for off_duty in results[1]:
                        print("不在岗的配送员：", off_duty)
        continue_find = input("是否继续查找？Y/N:")
        if continue_find == "N" or continue_find == "n":
            break

def update_delivery():
    """
    修改配送员状态
    :return:
    """
    while True:
        delivery_id = int(input("请输入配送员ID:"))
        with get_session() as session:
            delivery = DeliverymanRepository(session)
            result = delivery.find_by_id_update_status(p_id=delivery_id)
            if result[0]:
                if result[1] == 1:
                    print("修改状态成功，配送员状态修改为:在岗")
                if result[1] == 0:
                    print("修改状态成功，配送员状态修改为:休息")
            else:
                print("配送员不存在")
        continue_update = input("是否继续修改？Y/N:")
        if continue_update == "N" or continue_update == "n":
            break

def delivery_management():
    """
    配送员管理
    :return:
    """
    while True:
        print("----------------------- 配送员管理 -----------------------")
        print("---------------------- 1.添加配送员 ----------------------")
        print("---------------------- 2.查询配送员 ----------------------")
        print("--------------------- 3.修改配送员状态 --------------------")
        print("---------------------- 4.返回主菜单 ----------------------")
        menu_num = int(input("请输入编号选择："))
        match menu_num:
            case 1:
                add_delivery()
            case 2:
                find_delivery()
            case 3:
                update_delivery()
            case 4:
                break

def add_order():
    while True:
        """
        添加订单管理
        :return:
        """
        while True:
            product_id = int(input("请输入商品ID:"))
            delivery_id = int(input("请输入配送员ID:"))
            order_amount = int(input("请输入订单数量:"))
            order_address = input("请输入配送地址:")
            order_list = [OrderInfo(
                product_id=product_id,
                deliveryman_id=delivery_id,
                amount=order_amount,
                address=order_address
            )]
            with get_session() as session:
                order_info = OrderInfoRepository(session)
                state = order_info.get_all_order_infos(order_list)
                if state == -1:
                    print("商品库存不足")
                elif state == -2:
                    print("配送员不在岗")
                else:
                    print("订单添加成功")
            continue_add = input("是否继续添加？Y/N:")
            if continue_add == "N" or continue_add == "n":
                break

def find_order():
    """
    查询订单
    :return:
    """
    while True:
        print("---------------------- 查寻订单 ---------------------")
        print("------------------- 1.订单ID查找 -------------------")
        print("------------------- 2.订单状态查找 --------------------")
        print("------------------- 3.所有订单查找 -------------------")
        menu_num = int(input("请输入编号选择："))
        match menu_num:
            case 1:
                try:
                    order_id = int(input("请输入订单ID:"))
                except ValueError as e:
                    print(e)
                with get_session() as session:
                    order_info = OrderInfoRepository(session)
                    results = order_info.find_by_id_status_select_all_order_infos(o_id=order_id)
                    for result in results:
                        print(result)
            case 2:
                order_tmp = input("请输入订单状态询（待配送/配送中/已完成）:")
                order_state = 0
                if order_tmp == "待配送":
                    order_state = 0
                elif order_tmp == "配送中":
                    order_state = 1
                elif order_tmp == "已完成":
                    order_state = 2

                with get_session() as session:
                    order_info = OrderInfoRepository(session)
                    results = order_info.find_by_id_status_select_all_order_infos(o_status=order_state)
                    for result in results:
                        print(result)

            case 3:
                with get_session() as session:
                    order_info = OrderInfoRepository(session)
                    results = order_info.find_by_id_status_select_all_order_infos()
                    for result in results:
                        print(result)

        continue_find = input("是否继续查找？Y/N:")
        if continue_find == "N" or continue_find == "n":
            break


def update_order():
    """
    修改订单状态
    :return:
    """
    while True:
        try:
            order_id = int(input("请输入订单ID:"))
        except ValueError as e:
            print(e)
        with get_session() as session:
            order_info = OrderInfoRepository(session)
            result = order_info.find_by_id_update_status(o_id=order_id)
            if result:
                print("修改成功")
            else:
                print("配送员不存在")
        continue_update = input("是否继续修改？Y/N:")
        if continue_update == "N" or continue_update == "n":
            break

def cancel_order():
    """
    取消订单
    :return:
    """
    while True:
        try:
            order_id = int(input("请输入订单ID:"))
        except ValueError as e:
            print(e)
        with get_session() as session:
            order_info = OrderInfoRepository(session)
            result = order_info.find_by_id_update_cancel(o_id=order_id)
            if result == -1 :
                print("订单不存在")
            elif result == -2:
                print("无法取消该订单")
            else:
                print("取消订单成功")
        continue_update = input("是否继续取消？Y/N:")
        if continue_update == "N" or continue_update == "n":
            break


def order_management():
    """
    订单管理
    :return:
    """
    while True:
        print("----------------------- 订单管理 -----------------------")
        print("---------------------- 1.添加订单 ----------------------")
        print("---------------------- 2.查询订单 ----------------------")
        print("--------------------- 3.修改订单状态 --------------------")
        print("---------------------- 4.取消订单 -----------------------")
        print("---------------------- 5.返回主菜单 ---------------------")
        menu_num = int(input("请输入编号选择："))
        match menu_num:
            case 1:
                add_order()
            case 2:
                find_order()
            case 3:
                update_order()
            case 4:
                cancel_order()
            case 5:
                break

def main():
    """
    主界面
    :return:
    """
    while True:
        print("------------------ 社区生鲜配送管理系统 ------------------")
        print("---------------------- 1.商品管理 ----------------------")
        print("--------------------- 2.配送员管理 ---------------------")
        print("---------------------- 3.订单管理 ----------------------")
        print("---------------------- 4.退出系统 ----------------------")
        menu_num = int(input("请输入编号选择："))
        match menu_num:
            case 1:
                product_management()
            case 2:
                delivery_management()
            case 3:
                order_management()
            case 4:
                print("----------- 系统已退出，感谢使用! -----------")
                break


if __name__ == '__main__':
    """
    创建数据库表  
    """
    Base.metadata.create_all(engine)

    #主菜单
    main()
