"""
商品管理：
"""
from sqlalchemy import select

from model import Product,OrderInfo
from session import Session

class ProductRepository:
    def __init__(self,session:Session):
        self.session=session

    def get_all_products(self,products:list[Product]):
        """
        添加商品
        添加商品：输入商品名称、单价、初始库存，验证单价、库存为正数后，插入商品表，提示添加成功。
        :param products:
        :return:
        """
        logs = []
        for product in products:
            if product.price < 0:
                logs.append("价格不为正数"+product.name+"添加失败")
            elif product.stock < 0:
                logs.append("初始库存不为正数"+product.name + "添加成功")
            else:
                self.session.add(product)
                logs.append(product.name + "添加成功")
        return logs


    def find_by_id_or_name_and_all_product(self,p_id:int = None,p_name:str = None):
        """
        通过ID查找或者名字查找
        - 查询商品：支持按商品名称模糊查询、按商品ID精确查询，展示商品所有信息；
        也可查询所有商品，显示库存不足（≤5斤）的商品标记。
        :param p_id:
        :param p_name:
        :return:
        """
        if p_id:
            stat = select(Product).where(Product.id == p_id)
            result = self.session.execute(stat).all()
            return result
        elif p_name:
            stat = select(Product).where(Product.name.like("%"+p_name+"%"))
            result = self.session.execute(stat).all()
            return result
        else:
            stat = select(Product)
            result = self.session.execute(stat).all()

            stat = select(Product.name,Product.stock).where(Product.stock <= 5)
            flag = self.session.execute(stat).all()
            return result,flag

    def find_by_id_update_price_and_stock(self,p_id:int,p_price:float,p_stock:int):
        """
        修改商品
        - 修改商品：输入商品ID，验证商品存在后，可修改商品单价、库存（库存不能为负数），
        修改后提示成功。（7分）
        :param p_stock:
        :param p_price:
        :param p_id:
        :return:
        """
        stat = select(Product).where(Product.id == p_id)
        result = self.session.execute(stat).scalar_one_or_none()
        if not result:
            return False
        else:
            result.price = p_price
            result.stock = p_stock
            return True

    def find_by_id_delete_product(self,p_id:int):
        """
        删除商品
        - 删除商品：输入商品ID，验证商品存在且无关联订单（避免外键冲突）
        :param p_id:
        :return:
        """
        stat = select(Product).where(Product.id == p_id)
        result = self.session.execute(stat).scalar_one_or_none()
        if not result:
            return -1
        stat_check = select(OrderInfo).where(OrderInfo.product_id == p_id)
        related_item = self.session.execute(stat_check).scalar_one_or_none()
        if related_item:
            return -2

        self.session.delete(result)
        return True




