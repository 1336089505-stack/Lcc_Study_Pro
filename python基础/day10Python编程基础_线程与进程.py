"""
1.	编写一个函数，使用多线程实现并发下载任务。
函数签名：def concurrent_download(urls, max_workers=5)
要求：接收URL列表和最大工作线程数，
使用ThreadPoolExecutor下载每个URL的内容（可使用requests.get模拟），返回一个字典，
键为URL，值为状态码和内容长度（或None如果失败）。需要包含异常处理。
"""
import multiprocessing
from concurrent.futures import ThreadPoolExecutor

import requests

def download(url:str):
    try:
        response = requests.get(url, timeout=10)
        return {url, (response.status_code,len(response.content))}
    except Exception as e:
        print("下载失败：",url,e)
        return {url, None}

def concurrent_download(urls:list[str], max_workers=5):
    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        for url in urls:
            dict_tmp = pool.submit(download,url)
            print(dict_tmp.result())

"""2.	实现一个自定义线程池类，不依赖concurrent.futures。
要求：class SimpleThreadPool: 
包含submit方法提交任务，shutdown方法等待所有任务完成，
并能获取任务返回值。
内部使用queue.Queue传递任务，线程数量固定。
"""
import queue

class SimpleThreadPool:
    def __init__(self, max_workers: int = 5):
        """
        简化版线程池：固定线程数，支持提交任务、获取结果、等待任务完成
        :param max_workers: 线程数量，默认5
        """
        if max_workers <= 0:
            raise ValueError("max_workers 必须大于0")

        self.max_workers = max_workers
        self.task_queue = queue.Queue()  # 存储待执行的任务
        self.results = {}  # 存储任务结果 {task_id: 结果/异常}
        self.task_id = 0  # 任务ID计数器
        self.lock = threading.Lock()  # 保护results和task_id的线程安全
        self.shutdown_flag = False  # 是否关闭线程池

        #启动所有工作线程
        self._start_workers()

    def _start_workers(self):
        """启动指定数量的工作线程"""
        for _ in range(self.max_workers):
            # 守护线程：主线程退出时自动结束，避免阻塞程序退出
            worker = threading.Thread(target=self._worker, daemon=True)
            worker.start()

    def _worker(self):
        """工作线程逻辑：循环取任务执行"""
        while not self.shutdown_flag:
            try:
                # 队列为空时阻塞0.5秒，避免一直占用CPU检查shutdown_flag
                task = self.task_queue.get(block=True, timeout=0.5)
                task_id, func, args, kwargs = task

                # 执行任务并保存结果/异常
                try:
                    result = func(*args, **kwargs)
                    with self.lock:
                        self.results[task_id] = (True, result)  # (是否成功, 结果)
                except Exception as e:
                    with self.lock:
                        self.results[task_id] = (False, e)  # (是否成功, 异常)
                finally:
                    self.task_queue.task_done()  # 标记任务完成
            except queue.Empty:
                # 队列为空时，继续循环检查shutdown_flag
                continue

    def submit(self, func, *args, **kwargs):
        """
        提交任务
        :param func: 要执行的函数
        :return: 任务ID，用于后续获取结果
        """
        if self.shutdown_flag:
            raise RuntimeError("线程池已关闭，无法提交新任务")

        with self.lock:
            self.task_id += 1
            current_task_id = self.task_id

        # 将任务放入队列：(任务ID, 函数, 位置参数, 关键字参数)
        self.task_queue.put((current_task_id, func, args, kwargs))
        return current_task_id

    def get_result(self, task_id):
        """
        根据任务ID获取结果
        :param task_id: submit返回的任务ID
        :return: 任务执行结果；若执行失败，直接抛出异常
        """
        with self.lock:
            if task_id not in self.results:
                raise KeyError(f"任务ID {task_id} 不存在或未执行完成")

            success, data = self.results[task_id]
            if not success:
                raise data  # 抛出任务执行时的异常
            return data

    def shutdown(self):
        """关闭线程池，等待所有任务执行完成"""
        self.shutdown_flag = True
        # 等待队列中所有任务执行完毕
        self.task_queue.join()
        print("所有任务执行完成，线程池已关闭")


"""3.	编写一个函数，使用多进程并行计算指定范围内所有素数的个数。
函数签名：def parallel_prime_count(start, end, num_processes)
要求：将范围均匀分割成num_processes个子区间，使用multiprocessing.Pool.map或自定义进程池，
返回素数总数。需要实现is_prime辅助函数。
"""
from math import sqrt
import time
def parallel_prime_count(start, end, num_processes):
    def func(num_start, num_end):
        num_list = []
        num_tmp = num_start
        if num_start <= 2 :
            num_list.append(2)
            num_tmp = 3

        for num in range(num_tmp, num_end):
            check = True
            if num % 2 == 0:
                check = False
            else:
                num_s = int(sqrt(num)) + 1
                i = 3
                while i < num_s:
                    if num % i == 0:
                        check = False
                        break
                    i += 2
            if check:
                num_list.append(num)
        return num_list

    num_interval = ( end - start ) // num_processes
    pool = SimpleThreadPool()
    task_ids = []
    for i in range(0,num_processes-1):
        tid = pool.submit(func, start+num_interval*i, num_interval*(i+1)+1)
        task_ids.append(tid)
    tid = pool.submit(func, start+num_interval*(num_processes-1), end+1)
    task_ids.append(tid)

    time.sleep(1)
    for tid in task_ids:
        try:
            res = pool.get_result(tid)
            print(f"任务 {tid} 结果: {res}")
        except Exception as e:
            print(f"任务 {tid} 异常: {e}")

"""
4.	实现一个生产者-消费者模型，使用multiprocessing模块。
要求：一个生产者进程生成随机整数放入Queue，三个消费者进程从Queue取出数据并计算其平方，
将结果放入结果队列。主进程读取结果队列并打印。要求使用进程安全的方式终止消费者（如哨兵值）。
"""
import multiprocessing
import random
import time

# 定义哨兵值（用于通知消费者终止）
SENTINEL = None


def producer(queue, num_items):
    """
    生产者进程：生成指定数量的随机整数，放入队列
    :param queue: 存储原始数据的队列
    :param num_items: 要生成的随机数数量
    """
    print(f"生产者进程启动，将生成 {num_items} 个随机整数")
    for _ in range(num_items):
        # 生成1-100之间的随机整数
        random_num = random.randint(1, 100)
        queue.put(random_num)
        print(f"生产者放入: {random_num}")
        # 模拟生产耗时，让过程更直观
        time.sleep(0.1)

    # 放入哨兵值（数量等于消费者数量），确保每个消费者都能收到终止信号
    for _ in range(3):
        queue.put(SENTINEL)
    print("生产者已放入所有数据和哨兵值，生产完成")


def consumer(queue, result_queue, consumer_id):
    """
    消费者进程：从队列取数计算平方，结果放入结果队列，收到哨兵值则终止
    :param queue: 原始数据队列
    :param result_queue: 存储平方结果的队列
    :param consumer_id: 消费者ID，用于区分不同消费者
    """
    print(f"消费者 {consumer_id} 进程启动，等待处理数据...")
    while True:
        # 从队列取数据（阻塞式，直到取到数据）
        item = queue.get()

        # 检测哨兵值，收到则终止当前消费者
        if item == SENTINEL:
            print(f"消费者 {consumer_id} 收到哨兵值，准备终止")
            # 告知队列任务完成（避免主进程的join阻塞）
            queue.task_done()
            break

        # 计算平方
        square = item * item
        print(f"消费者 {consumer_id} 处理: {item} → 平方: {square}")
        # 将结果放入结果队列（格式：(原始数, 平方数, 消费者ID)）
        result_queue.put((item, square, consumer_id))

        # 标记队列任务完成（配合queue.join()使用）
        queue.task_done()

        # 模拟消费耗时
        time.sleep(0.2)

    print(f"消费者 {consumer_id} 正常终止")


def main():
    """主进程：创建队列、启动进程、读取结果并打印"""
    # 1. 创建进程安全的队列（multiprocessing.Queue是进程安全的）
    data_queue = multiprocessing.Queue()  # 存储原始随机数的队列
    result_queue = multiprocessing.Queue()  # 存储平方结果的队列

    # 2. 定义生产的随机数数量
    num_items = 10  # 可根据需要调整数量

    # 3. 创建并启动生产者进程
    producer_process = multiprocessing.Process(
        target=producer,
        args=(data_queue, num_items)
    )
    producer_process.start()

    # 4. 创建并启动3个消费者进程
    consumer_processes = []
    for i in range(3):
        consumer_proc = multiprocessing.Process(
            target=consumer,
            args=(data_queue, result_queue, i + 1)  # 消费者ID从1开始
        )
        consumer_processes.append(consumer_proc)
        consumer_proc.start()

    # 5. 等待生产者进程结束
    producer_process.join()
    print("=== 生产者进程已结束 ===")

    # 6. 等待所有消费者进程结束
    for proc in consumer_processes:
        proc.join()
    print("=== 所有消费者进程已结束 ===")

    # 7. 从结果队列读取并打印所有结果
    print("\n=== 最终计算结果 ===")
    results = []
    # 循环读取结果队列，直到为空
    while not result_queue.empty():
        results.append(result_queue.get())

    # 按原始数排序打印（可选，方便查看）
    results.sort(key=lambda x: x[0])
    for num, square, cid in results:
        print(f"原始数: {num} → 平方: {square} (由消费者 {cid} 计算)")

"""
5.	编写一个装饰器，用于测量函数在多线程环境下的执行时间。
要求：装饰器名timer，可以接受可选参数iterations（默认1），
对目标函数重复执行指定次数，分别使用单线程和多线程（线程数等于iterations），
打印两种方式的耗时对比。被装饰函数应为无参函数。
"""
import time
from typing import Callable

def timer(iterations: int = 1):
    """
    测量函数在单线程/多线程环境下执行时间的装饰器
    :param iterations: 重复执行的次数，默认1；需为正整数
    """
    # 参数校验：确保iterations是正整数
    if not isinstance(iterations, int) or iterations < 1:
        raise ValueError("iterations必须是大于等于1的整数")

    def decorator(func: Callable[[], None]) -> Callable[[], None]:
        def wrapper():
            # ------------------- 1. 单线程执行 -------------------
            print(f"\n=== 开始单线程执行（迭代{iterations}次）===")
            start_single = time.perf_counter()  # 高精度计时
            for _ in range(iterations):
                func()
            end_single = time.perf_counter()
            single_time = end_single - start_single

            # ------------------- 2. 多线程执行 -------------------
            print(f"\n=== 开始多线程执行（{iterations}个线程，每个线程执行1次）===")
            start_multi = time.perf_counter()
            # 创建线程列表：每个线程执行一次目标函数
            threads = [threading.Thread(target=func) for _ in range(iterations)]
            # 启动所有线程
            for t in threads:
                t.start()
            # 等待所有线程执行完成
            for t in threads:
                t.join()
            end_multi = time.perf_counter()
            multi_time = end_multi - start_multi

            # ------------------- 3. 打印耗时对比 -------------------
            print("\n=== 耗时对比结果 ===")
            print(f"迭代次数: {iterations}")
            print(f"单线程耗时: {single_time:.4f} 秒")
            print(f"多线程耗时: {multi_time:.4f} 秒")
            # 计算加速比（避免除以0）
            speedup = single_time / multi_time if multi_time > 0 else 0
            print(f"多线程加速比: {speedup:.2f} 倍")

        return wrapper

    return decorator


# ------------------- 测试用例 -------------------
# 定义一个模拟耗时的无参函数（用于测试装饰器）
@timer(iterations=5)  # 执行5次：单线程依次执行5次，多线程启动5个线程并发执行
def test_function():
    """模拟耗时操作（比如计算/IO）"""
    print(f"线程 {threading.current_thread().name} 执行test_function...")
    time.sleep(1)  # 模拟1秒耗时操作



"""
6.	实现一个读写锁类，支持多线程环境下的读优先或写优先（任选一种）。
要求：class ReadWriteLock: 
包含acquire_read, release_read, acquire_write, release_write方法。
允许多个读线程同时访问，写线程独占。需要避免写线程饥饿或读线程饥饿（根据选择的策略说明）
"""
import threading


class ReadWriteLock:
    """
    写优先的读写锁实现
    特性：
    1. 允许多个读线程同时持有读锁
    2. 写线程独占写锁（无读/其他写线程）
    3. 写优先：有写线程等待时，读线程需排队，避免写线程饥饿
    4. 通过条件变量控制线程等待/唤醒，避免读线程饥饿
    """

    def __init__(self):
        # 条件变量：用于线程的等待和唤醒（基于底层锁）
        self.condition = threading.Condition()

        # 状态变量
        self.read_count = 0  # 当前持有读锁的线程数
        self.write_active = False  # 是否有写线程正在持有写锁
        self.write_waiting = 0  # 等待获取写锁的线程数

    def acquire_read(self):
        """获取读锁（写优先：有写等待时，读线程排队）"""
        with self.condition:
            # 等待条件：无活跃写线程 且 无等待的写线程
            # 有写线程等待时，读线程优先让行，避免写线程饥饿
            while self.write_active or self.write_waiting > 0:
                self.condition.wait()

            # 满足条件，增加读线程计数
            self.read_count += 1

    def release_read(self):
        """释放读锁"""
        with self.condition:
            self.read_count -= 1
            # 读线程数为0时，通知等待的写线程
            if self.read_count == 0:
                self.condition.notify_all()

    def acquire_write(self):
        """获取写锁（独占）"""
        with self.condition:
            # 先标记有写线程等待（触发写优先逻辑）
            self.write_waiting += 1

            # 等待条件：无活跃读线程 且 无活跃写线程
            while self.read_count > 0 or self.write_active:
                self.condition.wait()

            # 满足条件，占用写锁
            self.write_active = True
            # 减少写等待数（当前线程已获取锁）
            self.write_waiting -= 1

    def release_write(self):
        """释放写锁"""
        with self.condition:
            self.write_active = False
            # 通知所有等待的线程（写优先：先唤醒写线程，再唤醒读线程）
            # 由于write_waiting的标记机制，新的读线程会先让行等待的写线程
            self.condition.notify_all()


# ------------------- 测试代码 -------------------
def read_worker(lock, thread_id):
    """读线程任务"""
    print(f"读线程 {thread_id} 尝试获取读锁...")
    lock.acquire_read()
    try:
        print(f"读线程 {thread_id} 持有读锁，开始读取...")
        threading.sleep(1)  # 模拟读操作耗时
        print(f"读线程 {thread_id} 完成读取，准备释放读锁")
    finally:
        lock.release_read()
        print(f"读线程 {thread_id} 已释放读锁")


def write_worker(lock, thread_id):
    """写线程任务"""
    print(f"写线程 {thread_id} 尝试获取写锁...")
    lock.acquire_write()
    try:
        print(f"写线程 {thread_id} 持有写锁，开始写入...")
        threading.sleep(1)  # 模拟写操作耗时
        print(f"写线程 {thread_id} 完成写入，准备释放写锁")
    finally:
        lock.release_write()
        print(f"写线程 {thread_id} 已释放写锁")

if __name__ == '__main__':
    """
    url_list = ["https://a56.gdl.netease.com/UURemote_Setup_4.16.1.6898_0207081559_baidu_pc_sem.exe?key1=e8d50fc75d974394726a3ba0ab8ae024&key2=6987ec3d&n=uuyc_4.16.1_baidu_pc_sem.exe",
                "https://www.zhihu.com",
                "https://www.sohu.com",
                "https://www.github.com",
                ]
    concurrent_download(url_list)
    """
    """parallel_prime_count(1,100,5)"""
    """test_function()"""
    print({1,2}<{1,2,3})


