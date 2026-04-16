"""
送员管理：
"""
from session import Session
from sqlalchemy import select

from model import Deliveryman


class DeliverymanRepository:
    def __init__(self, session:Session):
        self.session = session

    def get_all_deliveryman(self,deliveryman:list[Deliveryman]):
        """
        添加配送员
        - 添加配送员：输入配送员姓名、手机号（验证11位数字），插入配送员表，提示添加成功。
        :param deliveryman:
        :return:
        """
        logs = []
        for delivery in deliveryman:
            if len(delivery.phone) != 11:
                logs.append("配送员手机号不是11位")
            else:
                self.session.add(delivery)
                logs.append(delivery.name + "配送员添加成功")
        return logs

    def find_by_id_or_name_and_all_deliveryman(self, p_id: int = None, p_name: str = None):
        """
        通过ID查找或者名字查找
        - 查询配送员：支持按姓名模糊查询、按配送员ID精确查询，展示配送员所有信息；也可查询所有
        在岗/休息的配送员。
        :param p_id:
        :param p_name:
        :return:
        """
        if p_id:
            stat = select(Deliveryman).where(Deliveryman.id == p_id)
            result = self.session.execute(stat).all()
            return result
        elif p_name:
            stat = select(Deliveryman).where(Deliveryman.name.like("%" + p_name + "%"))
            result = self.session.execute(stat).all()
            return result
        else:
            stat = select(Deliveryman).where(Deliveryman.status == 1)
            on_duty = self.session.execute(stat).all()

            stat = select(Deliveryman).where(Deliveryman.status == 0)
            off_duty = self.session.execute(stat).all()
            return on_duty, off_duty

    def find_by_id_update_status(self,p_id:int):
        """
        修改配送员状态
        - 修改配送员状态：输入配送员ID，验证存在后，切换其状态（在岗↔休息），提示状态修改成功。
        修改后提示成功。（7分）
        :param p_id:
        :return:
        """
        stat = select(Deliveryman).where(Deliveryman.id == p_id)
        result = self.session.execute(stat).scalar_one_or_none()
        if not result:
            return False
        else:
            if result.status == 0:
                result.status = 1
            else:
                result.status = 0
            return True,result.status
