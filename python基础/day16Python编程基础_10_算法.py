"""
1.	编写一个函数 find_pythagorean_triples(n)，
找出所有满足 a^2 + b^2 = c^2 且 a+b+c <= n 的勾股三元组（a,b,c 为正整数，a<=b<c）。
返回列表，每个元素为 (a,b,c)。要求算法时间复杂度尽可能低。
"""
import math
import re
def find_pythagorean_triples(n):
    max_a = n // 3
    triples_list = []
    for i in range(1, max_a+1):
        max_b = (n - i)//2
        for j in range(1, max_b+1):
            k_sqrt = i**2 + j**2
            k =  int(math.isqrt(k_sqrt))
            if k*k == k_sqrt and (i+j+k) <= n and i <= j:
                 triples_list.append([i, j, k])
    return triples_list


"""
2.	编写一个函数 max_subarray_sum(arr)，
使用分治法或动态规划（Kadane算法）求给定整数数组的最大子数组和。
返回最大和值。要求实现O(n)算法。
"""
def max_subarray_sum(arr):
    if not arr:
        return 0  # 或抛出异常：raise ValueError("数组不能为空")

        # 初始化：当前子数组最大和、全局最大和均为第一个元素
    current_max = global_max = arr[0]

    # 遍历数组（从第二个元素开始），O(n)时间
    for num in arr[1:]:
        # 状态转移：选择延续前一个子数组 或 重新开始子数组
        current_max = max(num, current_max + num)
        # 更新全局最大和
        if current_max > global_max:
            global_max = current_max

    return global_max


"""
3.	编写一个函数 is_palindrome(s)，
判断字符串s是否为回文（忽略大小写和非字母数字字符）。
例如 "A man, a plan, a canal: Panama" 返回True。
要求使用双指针法。
"""
def is_palindrome(s):
    s_tmp = s.lower()
    pattern = r'[^a-z]'
    clean_text = re.sub(pattern, '', s_tmp)
    for i in range(len(clean_text)//2):
        if clean_text[i] != clean_text[-(i+1)]:
            return False
    return True

"""
4.	编写一个函数 count_sort(arr)，实现计数排序，对非负整数列表进行升序排序。
返回排序后的列表。要求时间复杂度O(n+k)，其中k为最大值。
"""
def count_sort(arr):
    if not arr:
        return []
    
    max_val = max(arr)
    count = [0] * (max_val + 1)
    
    for num in arr:
        count[num] += 1
    
    result = []
    for i in range(len(count)):
        result.extend([i] * count[i])
    
    return result

"""
5.	编写一个函数 binary_search(arr, target)，在有序列表arr中二分查找目标值target，
返回索引，若不存在返回-1。要求递归或迭代实现。
"""
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


"""
6.	编写一个函数 factorial(n)，计算n的阶乘，n为非负整数。
要求使用递归实现，并考虑大数情况（Python支持大整数）。返回整数。
"""
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    print(left, middle, right)
    return quick_sort(left) + middle + quick_sort(right)


if __name__ == '__main__':
    print(find_pythagorean_triples(12))
    print(is_palindrome("A man, a plan, a canal: Panama"))
    print(count_sort([4, 2, 2, 8, 3, 3, 15, 1]))

    print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
    print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 10))

    print(quick_sort([54,26,93,17,77,31,44,55,20]))

    #冒泡排序
    """
    a = [54,26,93,17,77,31,44,55,20]
    for i in range(len(a)-1,0,-1):
        for j in range(i):
            if a[j] > a[i]:
                a[i], a[j] = a[j], a[i]
    print(a)
    """

    #选择排序
    """
    a = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    n = len(a)
    # 需要进行 n-1 次选择操作
    for i in range(n - 1):
        # 记录最小位置
        min_index = i
    # 从 i+1 位置到末尾选择出最小数据
        for j in range(i + 1, n):
            if a[j] < a[min_index]:
                min_index = j
    # 如果选择出的数据不在正确位置，进行交换
        if min_index != i:
            a[i], a[min_index] = a[min_index], a[i]
    print(a)
    """

    #插入排序
    """
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    n = len(alist)
    for j in range(1, n):
        i = j
        while i > 0:
            if alist[i] < alist[i - 1]:
                alist[i], alist[i - 1] = alist[i - 1], alist[i]
            else:
                break
            i-=1
    print(alist)
    """

    #快速排序





