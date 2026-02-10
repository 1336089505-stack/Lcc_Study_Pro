"""
定义一个Student类。
要求：
使用__init__方法初始化学生的name（姓名）和__score（私有属性，成绩）。
使用@property和@score.setter实现一个名为score的属性。
getter返回成绩。
setter在设置成绩时进行验证：成绩必须在0到100之间（包含0和100），
否则抛出ValueError异常，并提示“成绩必须在0-100之间”。
实现__str__方法，返回字符串如：“学生张三，成绩：85”。
编写代码创建Student对象，尝试设置合法和非法的成绩，并打印学生信息。
"""
import warnings

class Student:
    def __init__(self,name,score):
        self.name = name
        self.__score = score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self,value):
        if value < 0 or value > 100:
            raise ValueError("参数类型错误")
        else:
            self.__score = value

    def __str__(self):
        return f"学生{self.name},成绩{self.__score}"


"""
2.	设计一个Singleton类（单例模式）。
要求：
•	重写__new__方法，确保这个类在整个程序中最多只有一个实例。
•	提示：在__new__中，检查类是否已经有一个实例存储在类属性中（例如_instance），如果没有，则调用父类的__new__创建并存储；如果有，则直接返回存储的实例。
•	提供一个__init__方法用于初始化（注意：在单例模式中，__init__可能会被多次调用，
    需要小心处理，例如可以设置一个标志位_initialized来避免重复初始化）。
•	在__init__中接受一个value参数，并将其赋值给实例的data属性。
编写代码测试，创建两个Singleton对象，检查它们是否是同一个对象（id()是否相同），并打印它们的data属性。
"""

"""
class Singleton:
    _instance = None
    _initialized = False
    def __new__(cls,*args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value):
        if not self._initialized:
            self.data = value
            self._initialized = True
            return
"""


"""
3.	实现一个LimitedInstances类。
要求：
•	这个类限制最多只能创建3个实例。
•	重写__new__方法，在创建新实例前进行检查。
•	使用一个类属性（例如_instances列表）来跟踪已创建的实例。
•	如果当前实例数量未达到上限（3个），则创建新实例并将其加入列表，然后返回。
•	如果已达到上限，则抛出RuntimeError异常，提示“已达到最大实例数量限制（3个）”。
•	注意：需要考虑实例被销毁（del）的情况，以释放名额。可以在__del__方法中将实例从列表中移除（注意：__del__的调用时机不确定，此题为简化逻辑，假设在del对象后立即调用）。
编写代码测试，尝试创建第4个实例，观察是否抛出异常。
"""
class LimitedInstances:
    _instances = []
    def __new__(cls, *args, **kwargs):#给这个类分配一个内存空间，返回这个实例的对象
        if len(cls._instances) < 3:
            inside = super().__new__(cls)
            cls._instances.append(inside)
        else:
            raise RuntimeError("已达到最大实例数量限制（3个）")
        print(inside)
        return super().__new__(cls)

    def __init__(self,data):
        self.data = data


    def __del__(self):
        print(f"❌ 销毁对象: {self.data}")
        print(self,self._instances)
        if self in self._instances:
            self._instances.remove(self)



"""
创建一个Vector2D类表示二维向量(x， y)。
要求：
在__init__中初始化x和y。
实现__add__特殊方法，支持两个向量相加（x相加，y相加），返回一个新的Vector2D对象。
实现__sub__特殊方法，支持两个向量相减。
实现__mul__特殊方法，支持向量与标量（数字）相乘（x和y分别乘以标量），返回新向量。
实现__str__方法，返回如“(3.0， 4.0)”的字符串。
实现__repr__方法，返回如“Vector2D(3.0， 4.0)”的字符串，使得eval(repr(v))能创建一个相同的向量。
编写代码测试向量的加、减、标量乘法，并打印其str和repr表示。
"""
class Vector2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self,x,y):
        return Vector2D(self.x+x,self.y+y)
    def __sub__(self,x,y):
        return Vector2D(self.x-x,self.y-y)
    def __mul__(self,x,y):
        return Vector2D(self.x*x,self.y*y)
    def __str__(self):
        return f"({self.x},{self.y})"
    def __repr__(self):
        return f"({self.x},{self.y})"


"""
实现一个FileHandler上下文管理器类（模拟）。
这个类不是使用with语句和__enter__， __exit__， 而是模拟资源管理。
类有__init__方法，接受一个filename参数。
有open方法，打印“打开文件 [filename]”， 并将一个标志_is_open设为True。
有close方法，打印“关闭文件 [filename]”， 并将_is_open设为False。
实现__del__方法。在__del__中，如果文件还未关闭（_is_open为True）， 
则自动调用close方法并打印警告信息：“警告：对象被销毁时文件未关闭，已自动关闭。”
编写代码测试：创建一个FileHandler对象，调用open但不调用close，
然后删除对象或让对象离开作用域，观察__del__的行为。再测试正常open和close的情况。
"""
class FileHandler:
    _is_open = False
    def __init__(self,filename):
        self.filename = filename
    def open(self):
        print(f"打开文件{self.filename}")
        self._is_open = True
    def close(self):
        print(f"关闭文件{self.filename}")
        self._is_open = False


    def __del__(self):
        self.close()
        warnings.warn("警告：对象被销毁时文件未关闭，已自动关闭。")




if __name__ == '__main__':
    """
    student_lcc = Student('LCC',40)
    #非法
    #student_lcc.__score = 50
    #合法
    student_lcc.score = 100
    print(student_lcc)
    """

    """
    sing1 = Singleton(100)
    sing2 = Singleton(200)
    print(id(sing1))
    print(id(sing2))
    print(sing1.data)
    print(sing2.data)
    """

    """
    limited1 =  LimitedInstances(1)
    limited1.__del__()
    del limited1
    limited2 = LimitedInstances(2)
    limited3 = LimitedInstances(3)
    """
    """
    vector1 = Vector2D(3,4)
    a = vector1.__add__(3,4)
    print(a.__str__())
    print(a.__repr__())
    b = vector1.__sub__(3,4)
    print(b.__str__())
    print(b.__repr__())
    c = vector1.__mul__(3,4)
    print(c.__str__())
    print(c.__repr__())
    """
    """
    file1 = FileHandler("file1.txt")
    file2 = FileHandler("file2.txt")
    file1.open()
    file1.__del__()
    del file1
    """
    pass