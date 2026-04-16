"""
订单管理：
"""
from session import Session
from sqlalchemy import select

from model import OrderInfo,Product,Deliveryman


class OrderInfoRepository():
    def __init__(self, session:Session):
        self.session = session

    def get_all_order_infos(self,order_infos:list[OrderInfo]):
        """
        添加配送员
        - 创建订单：输入商品ID、配送员ID、订单数量、配送地址，验证商品存在且库存充足、配送员在
        岗后，计算订单总金额，插入订单表，同时扣减对应商品的库存，提示订单创建成功。
        :param order_infos:
        :return:
        """
        for order_info in order_infos:
            stat = select(Product).where(Product.id == order_info.product_id)
            pro_result = self.session.execute(stat).scalar_one_or_none()
            if pro_result.stock < order_info.amount:
                return -1
            stat = select(Deliveryman).where(Deliveryman.id == order_info.deliveryman_id)
            del_result = self.session.execute(stat).scalar_one_or_none()
            if del_result.status == 0:
                return -2

            order_info.total = order_info.amount * pro_result.price
            pro_result.stock = pro_result.stock - order_info.amount

            self.session.add(order_info)
            return True

    def find_by_id_status_select_all_order_infos(self,o_id:int = None,
                                                 o_status:int = None):
        """
        - 查询订单：支持按订单ID精确查询、按订单状态查询（待配送/配送中/已完成），展示订单所有信
        息（关联显示商品名称、配送员姓名，而非仅显示ID）。（7分）
        """
        if o_id:
            stat = (select(OrderInfo,Product.name,Deliveryman.name)
                    .where(OrderInfo.id == o_id)
                    .join(Deliveryman,Deliveryman.id == OrderInfo.deliveryman_id)
                    .join(Product,Product.id == OrderInfo.product_id))
            result = self.session.execute(stat).all()
            return result
        elif o_status:
            stat = (select(OrderInfo,Product.name,Deliveryman.name)
                    .where(OrderInfo.status == o_status)
                    .join(Product).join(Deliveryman))
            result = self.session.execute(stat).all()
            return result
        else:
            stat = (select(OrderInfo,Product.name,Deliveryman.name)
                    .join(Product).join(Deliveryman))
            result = self.session.execute(stat).all()
            return result


    def find_by_id_update_status(self,o_id:int):
        """
        修改订单状态
        - 修改订单状态：输入订单ID，验证订单存在后，可修改订单状态（如：待配送→配送中、配送中→
        已完成），提示修改成功。（7分）
        :param o_id:
        :return:
        """
        stat = (select(OrderInfo).where(OrderInfo.id == o_id))
        result = self.session.execute(stat).scalar_one_or_none()
        if not result:
            return False
        result.status = result.status + 1
        return True


    def find_by_id_update_cancel(self,o_id:int):
        """
        - 取消订单：输入订单ID，验证订单状态为“待配送”后，取消订单（修改状态为3），同时将订单
        对应的商品库存恢复，提示取消成功；若订单已处于配送中/已完成，提示“无法取消该订单”。
        :param o_id:
        :return:
        """
        stat = (select(OrderInfo).where(OrderInfo.id == o_id))
        result = self.session.execute(stat).scalar_one_or_none()
        if not result:
            return -1
        if result.status != 0:
            return -2
        result.status = 3

        stat = select(Product).where(Product.id == result.product_id)
        pro_result = self.session.execute(stat).scalar_one_or_none()
        pro_result.stock = pro_result.stock + result.amount

        return True


