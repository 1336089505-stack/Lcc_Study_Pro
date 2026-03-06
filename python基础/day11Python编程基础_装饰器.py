"""1.	编写一个装饰器函数 @cache_result，实现简单的内存缓存功能。
要求：支持任意参数的位置参数和关键字参数，缓存在指定时间后过期。
函数签名：def cache_result(timeout=60)。
被装饰的函数可以是任意返回可哈希值的函数。需要处理可变参数作为键时的问题。
"""
"""
import time
import functools

def cache_result(timeout=60):
    # 外层接收超时参数，返回真正的装饰器
    def decorator(func):
        cache = {}  # 缓存结构：key → (result, expire_time)

        @functools.wraps(func)
        def wrapper(*args):
            key = args
            now = time.time()

            # 检查缓存是否存在且未过期
            if key in cache and now < cache[key][1]:
                print(f"✅ 命中缓存：{key} → {cache[key][0]}")
                return cache[key][0]

            # 执行函数，保存结果和过期时间
            print(f"🔄 执行函数：{key}")
            result = func(*args)
            cache[key] = (result, now + timeout)
            return result

        return wrapper

    return decorator

@cache_result(1)
def add(a, b):
    return a + b
print(add(1, 2))
print(add(1, 2))
time.sleep(1)  
print(add(1, 2))
"""

"""
2.	实现一个自定义的Range类，使其支持迭代器和切片操作。
要求：实现__iter__和__next__方法，使其可以像内置range一样惰性生成数字；
实现__getitem__方法，支持索引访问和切片返回新的Range对象。不依赖内置range的实现。
"""
class Range:
    def __init__(self, start, stop=None, step=1):
        if stop is None:
            self.start = 0
            self.stop = start
        else:
            self.start = start
            self.stop = stop
        self.step = step
        if self.step == 0:
            raise ValueError("step must be greater than 0")
    def __iter__(self):
        current = self.start
        while (( self.step > 0 and current < self.stop) or
               (current > self.stop and self.step < 0)):
            yield current
            current += self.step
    def __len__(self):
        # 计算长度（用于索引校验）
        if (self.step > 0 and self.start >= self.stop) or (self.step < 0 and self.start <= self.stop):
            return 0
        return (abs(self.stop - self.start) - 1) // abs(self.step) + 1

    def __getitem__(self, index):
        # 实现索引访问
        if index < 0:
            index = len(self) + index  # 处理负索引
        if not (0 <= index < len(self)):
            raise IndexError("Range index out of range")
        # 直接计算索引对应的数值（不用遍历）
        return self.start + index * self.step

print("Range遍历：", list(Range(5,0,-2)))

"""
3.	编写一个函数 group_by，用于对可迭代对象进行分组。
函数签名：def group_by(iterable, key_func)。
要求：返回一个字典，键为key_func作用于元素的结果，值为该分组下所有元素组成的列表。
需要保持每个分组内元素的原始相对顺序。不能使用itertools.groupby。
"""
from typing import Iterable, Callable, Dict, List, Any
def group_by(iterable, key_func):
    result = {}
    for item in iterable:
        key = key_func(item)
        if key not in result:
            result[key] = []
        result[key].append(item)
    return result

"""
4.	实现一个简单的观察者模式，使用函数实现。
要求：定义Observable类，包含subscribe、unsubscribe、notify方法。
订阅者是一个接收一个参数的函数。
当notify(data)被调用时，所有已订阅的函数被调用，参数为data。
要求线程安全（考虑多线程场景）。
"""
import threading
from typing import Callable, List, Any


class Observable:
    """
    线程安全的观察者模式实现类
    支持订阅、取消订阅、通知所有订阅者，且单个订阅者执行异常不影响其他订阅者
    """

    def __init__(self):
        # 存储订阅者函数的列表
        self._subscribers: List[Callable[[Any], None]] = []
        # 可重入锁（RLock）保证线程安全：支持同一线程多次获取锁，避免死锁
        self._lock = threading.RLock()

    def subscribe(self, subscriber: Callable[[Any], None]) -> None:
        """
        订阅观察者：添加一个接收单个参数的函数到订阅列表

        Args:
            subscriber: 订阅者函数，签名为 func(data)
        """
        if not callable(subscriber):
            raise TypeError("subscriber must be a callable function")

        # 加锁保护订阅列表的修改（多线程下防止竞态条件）
        with self._lock:
            # 避免重复订阅（可选逻辑，根据需求可移除）
            if subscriber not in self._subscribers:
                self._subscribers.append(subscriber)

    def unsubscribe(self, subscriber: Callable[[Any], None]) -> None:
        """
        取消订阅：从订阅列表移除指定函数

        Args:
            subscriber: 要取消订阅的函数
        """
        # 加锁保护订阅列表的修改
        with self._lock:
            if subscriber in self._subscribers:
                self._subscribers.remove(subscriber)

    def notify(self, data: Any) -> None:
        """
        通知所有订阅者：调用每个订阅者函数，传入data参数
        特性：
        1. 线程安全：遍历订阅列表的副本，避免遍历中列表被修改
        2. 容错性：单个订阅者报错不影响其他订阅者执行
        """
        # 加锁获取订阅列表的副本（避免遍历过程中列表被修改导致异常）
        with self._lock:
            # 复制列表，遍历副本而非原列表
            subscribers_copy = self._subscribers.copy()

        # 遍历副本并调用订阅者函数，逐个捕获异常
        for subscriber in subscribers_copy:
            try:
                subscriber(data)
            except Exception as e:
                # 打印异常但不中断其他订阅者执行（可根据需求调整异常处理逻辑）
                print(f"Subscriber function raised an exception: {e}")

    def get_subscriber_count(self) -> int:
        """获取当前订阅者数量（辅助方法，用于测试/调试）"""
        with self._lock:
            return len(self._subscribers)

"""
5.	编写一个函数 flatten，用于展开嵌套的可迭代对象。
函数签名：def flatten(nested_iterable, depth=None)。
要求：depth参数指定展开深度，None表示完全展开。
支持任意层级的嵌套，元素可以是列表、元组、集合等可迭代对象，
但字符串不展开（视为原子）。返回生成器，惰性产生元素。
"""
def flatten(nested_iterable, depth=None):
    for item in nested_iterable:
        if (depth is None or depth > 0 ) and isinstance(item, Iterable) and not isinstance(item, (str, bytes)):
            yield from flatten(item, depth-1 if depth else None)
        else:
            yield item

"""
6.实现一个函数 compose，用于函数组合。
函数签名：def compose(*funcs)。
要求：返回一个新函数，该函数从右向左依次应用给定的函数（数学组合顺序）。
例如compose(f, g, h)(x) = f(g(h(x)))。
支持任意数量的函数，若未提供参数则返回恒等函数。
需要处理函数签名和文档字符串的保留。
"""
import functools


def compose(*funcs):
    """
    函数组合：从右向左依次应用传入的函数。

    参数:
        *funcs: 待组合的函数序列（任意数量）

    返回:
        新函数：依次执行funcs中的函数（从右到左），无funcs时返回恒等函数

    示例:
        >>> f = lambda x: x + 1
        >>> g = lambda x: x * 2
        >>> h = lambda x: x - 3
        >>> composed = compose(f, g, h)
        >>> composed(10)  # f(g(h(10))) = (10-3)*2 +1 = 15
        15
    """
    # 处理无函数的情况：返回恒等函数
    if not funcs:
        return lambda x: x

    def composed_func(x):
        # 核心逻辑：从右向左执行函数（先反转funcs，再依次应用）
        # 等价于：先执行最后一个函数，结果传给倒数第二个，直到第一个
        result = x
        # reversed(funcs) 把 (f,g,h) 变成 (h,g,f)，依次执行
        for func in reversed(funcs):
            result = func(result)
        return result

    # 保留函数的元信息（签名、文档等），让composed_func更规范
    functools.wraps(composed_func)(composed_func)
    return composed_func


if __name__ == "__main__":
    #1
    #2
    """
    nested1 = [1,2,[3,4,[5,6,[7,8,9],8],[7,6,5],[4],[3]],[2,1]]
    a_list = list(flatten(nested1,2))
    print(a_list)
    """
    #3
    """
    a = ["abc", "asdasd", "asdasdada", "123", "5"]
    b = group_by(a, len)
    print(b)
    """