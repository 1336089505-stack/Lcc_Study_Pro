class PrimeIterator:
    """
    质数迭代器，用于生成指定范围内的所有质数
    """
    
    def __init__(self, start, end):
        """
        初始化迭代器
        
        参数:
            start: 起始范围
            end: 结束范围
        """
        self.start = start
        self.end = end
        self.current = start
    
    def __iter__(self):
        """
        返回迭代器自身
        """
        return self
    
    def __next__(self):
        """
        返回下一个质数，超出范围则抛出 StopIteration
        """
        # 从当前位置开始寻找下一个质数
        while self.current <= self.end:
            num = self.current
            self.current += 1
            if self._is_prime(num):
                return num
        # 超出范围，抛出异常
        raise StopIteration
    
    def _is_prime(self, n):
        """
        判断一个数是否为质数
        
        参数:
            n: 要判断的数
        
        返回:
            bool: 是否为质数
        """
        # 质数定义：大于1的自然数，除了1和自身外没有其他因数
        if n <= 1:
            return False
        # 2是最小的质数
        if n == 2:
            return True
        # 偶数不是质数
        if n % 2 == 0:
            return False
        # 检查从3到sqrt(n)的奇数
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True


# 测试代码
def test_prime_iterator():
    print("=== 测试质数迭代器 ===")
    
    # 测试 1-20 之间的质数
    print("\n1. 测试 1-20 之间的质数:")
    primes_1_20 = list(PrimeIterator(1, 20))
    print(f"结果: {primes_1_20}")
    print(f"期望: [2, 3, 5, 7, 11, 13, 17, 19]")
    
    # 测试 20-50 之间的质数
    print("\n2. 测试 20-50 之间的质数:")
    primes_20_50 = list(PrimeIterator(20, 50))
    print(f"结果: {primes_20_50}")
    print(f"期望: [23, 29, 31, 37, 41, 43, 47]")
    
    # 测试 start > end 的情况
    print("\n3. 测试 start > end 的情况:")
    primes_empty = list(PrimeIterator(10, 5))
    print(f"结果: {primes_empty}")
    print(f"期望: []")
    
    # 测试单个质数的情况
    print("\n4. 测试单个质数的情况:")
    primes_single = list(PrimeIterator(2, 2))
    print(f"结果: {primes_single}")
    print(f"期望: [2]")
    
    # 测试无质数的情况
    print("\n5. 测试无质数的情况:")
    primes_none = list(PrimeIterator(4, 6))
    print(f"结果: {primes_none}")
    print(f"期望: [5]")


if __name__ == "__main__":
    test_prime_iterator()