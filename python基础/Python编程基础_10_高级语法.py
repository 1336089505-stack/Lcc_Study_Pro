"""
1.	实现一个深拷贝函数 deep_copy(obj)，
不使用 copy 模块，能够处理列表、字典和基本数据类型。
要求递归实现，处理循环引用。
"""

def deep_copy(obj):
    if isinstance(obj, list):
        obj_tmp = []
        for i in range(len(obj)):
            obj_tmp.append(deep_copy(obj[i]))
        return obj_tmp
    elif isinstance(obj, dict):
        obj_tmp = {}
        for k, v in obj.items():
            obj_tmp[k] = deep_copy(v)
        return obj_tmp
    elif isinstance(obj, (int, float, bool,str,type(None))):
        return obj
    else:
        return obj


"""
2.	编写一个迭代器类 PrimeIterator，用于生成指定范围内的所有质数。
实现 iter() 和 next() 方法。
"""
from math import sqrt
class PrimeIterator(object):
    def __init__(self, obj):
        self.obj = obj
        self.index = 0
    def __iter__(self):
        return self
    def _is_prime(self, num):
        if num == 1:
            return False
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True
    def __next__(self):
        while True:
            if self.index < len(self.obj):
                item = self.obj[self.index]
                self.index += 1
                if self._is_prime(int(item)):
                    return item
            else:
                raise StopIteration

"""
3.	实现一个生成器函数 fibonacci(n)，生成斐波那契数列的前 n 项。
要求使用生成器实现，避免一次性生成所有值。
"""

def fibonacci(n):
    a, b, counter = 0, 1, 0
    while counter < n:
        print(a, b,counter)
        yield b
        a, b, counter = b, a + b, counter + 1
    return "done"

"""
4.	编写一个闭包函数 counter()，每次调用返回一个递增的整数。
要求不使用全局变量，每次调用 counter() 返回的函数都能记住当前计数值。
"""
def counter():
    n = 0
    def count():
        nonlocal n
        n += 1
        return n
    return count


"""
5.	实现一个装饰器 timer，用于测量函数的执行时间。
装饰器应该输出函数名和运行时间（秒），并保留原函数的元信息。
"""
import time
def timer(fun):
    def time_s():
        start_time = time.time()
        print("函数名:",fun.__name__)
        fun()
        print("运行时间:",round(time.time() - start_time , 1))
    return time_s


@timer
def test():
    for i in range(1000):
        for i in range(1000):
            print(i)


if __name__ == '__main__':
    """
    list1 = [1, 2, 3]
    print(id(list1), id(list1[0]), id(list1[1]), id(list1[2]))
    list2 = deep_copy(list1)
    print(list2)
    print(id(list2), id(list2[0]), id(list2[1]), id(list2[2]))
    """

    """
    list1 = [i for i in range(100)]
    iters = PrimeIterator(list1)
    for item in iters:
        print(item)
    """

    """
    for i in fibonacci(10):
        print(i)
    """

    """
    a = counter()
    for i in range(10):
        print(a())
    """

    test()