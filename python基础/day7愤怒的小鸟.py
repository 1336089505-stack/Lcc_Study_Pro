class Birds:
    def __init__(self,bird_name,bird_color,bird_skill_description):
        """
        name：用于标识每只小鸟的名称，方便区分不同个体。
        color：代表小鸟的颜色，这是小鸟的一个显著特征，在游戏中可以对应不同类型的小鸟。
        skill_description：描述小鸟所具备的独特技能，让玩家了解每只小鸟的特殊能力。
        """
        self.name = bird_name
        self.color = bird_color
        self.skill_description = bird_skill_description

        #fly()：描述小鸟飞行的基本动作，是小鸟在游戏中的常见行为，所有子类都可以重写该
        #call()：模拟小鸟发出叫声的行为，同样可以被子类重写以体现不同小鸟的叫声差异。
        #use_skill()：用于触发小鸟的特殊技能，展示小鸟使用技能的情况，子类可以根据自身技能特点进行相应实现。
    def fly(self):
        """
        飞
        :return:
        """
        return f"{self.name}飞行"
    def call(self):
        """
        叫
        :return:
        """
        return f"{self.name}发出叫声"
    def use_skill(self):
        return f"{self.name}使用{self.skill_description}"

"""
通过调用基类的 __init__ 方法，初始化各自的 name、color 和 skill_description 属性，确保每只小鸟都有自己的独特标识和技能。
fly()：重写基类的 fly() 方法，展示不同小鸟的飞行特点，如红鸟以稳定速度飞行，黄鸟快速飞行，蓝鸟优雅飞行。
call()：重写基类的 call() 方法，模拟不同小鸟的叫声，增加游戏的趣味性。
"""
class RedBirds(Birds):
    def __init__(self):
        super().__init__(bird_name='red_bird',
                         bird_color='red',
                         bird_skill_description='普通攻击技能')

    def fly(self):
        """
        飞行
        :return:
        """
        return f"{self.name}稳定速度飞行"
    def call(self):
        """
        叫声
        :return:
        """
        return f"{self.name}发出红色叽叽叽叫声"

class YellowBirds(Birds):
    def __init__(self):
        super().__init__(bird_name='yellow_bird',
                         bird_color='yellow',
                         bird_skill_description='爆炸技能')
    def fly(self):
        """
        飞
        :return:
        """
        return f"{self.name}稳定快速飞行"
    def call(self):
        """
        叫
        :return:
        """
        return f"{self.name}发出黄色咕咕咕叫声"

class BlueBirds(Birds):
    def __init__(self):
        super().__init__(bird_name='blue_bird',
                         bird_color='blue',
                         bird_skill_description='分裂技能')
    def fly(self):
        """
        飞行
        :return:
        """
        return f"{self.name}稳定优雅飞行"
    def call(self):
        """
        叫声
        :return:
        """
        return f"{self.name}发出蓝色啾啾啾叫声"

"""
代表游戏中的障碍物，如木头堡垒、石头塔楼等，负责处理障碍物被小鸟攻击的逻辑，与小鸟类进行交互，体现了面向对象编程中的对象交互和封装思想。
name：标识障碍物的名称，方便区分不同类型的障碍物。
strength：表示障碍物的强度，即它能够承受的伤害值，当强度降为 0 时，障碍物被摧毁。
be_attacked(bird)：模拟障碍物被小鸟攻击的过程，根据小鸟的类型计算伤害，并更新障碍物的强度，同时输出攻击和受损信息，让玩家了解游戏进展。
"""

class Obstacle:
    def __init__(self,obstacle_name,obstacle_strength):
        self.name = obstacle_name
        self.strength = obstacle_strength

    bird_damage = {
        "red_bird": 10,
        "yellow_bird": 15,
        "blue_bird": 5
    }
    def be_attacked(self,bird:Birds):
        """
        伤害过程
        :param bird:
        :return:
        """
        damage = self.bird_damage.get(bird.name)
        self.strength = self.strength - damage

        attack_info = f"{bird.name}攻击了{self.name},造成了{damage}点伤害,{self.name}剩余强度：{self.strength}"

        if self.strength <= 0:
            attack_info += f",{self.name}强度为0被摧毁！"
        return attack_info

if __name__ == '__main__':

    #实例化
    red1 = RedBirds()
    blue1 = BlueBirds()
    yellow1 = YellowBirds()
    m_box = Obstacle("木箱子",50)

    #飞行
    print(red1.fly())
    print(yellow1.fly())
    print(blue1.fly())

    #叫声
    print(red1.call())
    print(yellow1.call())
    print(blue1.call())

    #放技能
    print(red1.use_skill())
    print(blue1.use_skill())
    print(yellow1.use_skill())

    #障碍物伤害过程
    print(m_box.be_attacked(red1))
    print(m_box.be_attacked(red1))
    print(m_box.be_attacked(blue1))
    print(m_box.be_attacked(blue1))
    print(m_box.be_attacked(yellow1))
    print(m_box.be_attacked(yellow1))