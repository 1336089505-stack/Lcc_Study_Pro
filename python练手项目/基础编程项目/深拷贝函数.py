def deep_copy(obj, memo=None):
    """
    深拷贝函数，处理列表、字典和基本数据类型，支持循环引用
    
    参数:
        obj: 要拷贝的对象
        memo: 用于记录已拷贝对象的映射表，避免循环引用
    
    返回:
        拷贝后的新对象
    """
    # 初始化映射表
    if memo is None:
        memo = {}
    
    # 处理基本数据类型（不可变类型）
    if isinstance(obj, (int, float, str, bool, type(None))):
        return obj
    
    # 处理列表
    elif isinstance(obj, list):
        # 检查是否已拷贝过
        if id(obj) in memo:
            return memo[id(obj)]
        # 创建新列表
        new_list = []
        # 记录到映射表
        memo[id(obj)] = new_list
        # 递归拷贝每个元素
        for item in obj:
            new_list.append(deep_copy(item, memo))
        return new_list
    
    # 处理字典
    elif isinstance(obj, dict):
        # 检查是否已拷贝过
        if id(obj) in memo:
            return memo[id(obj)]
        # 创建新字典
        new_dict = {}
        # 记录到映射表
        memo[id(obj)] = new_dict
        # 递归拷贝每个键值对
        for key, value in obj.items():
            new_dict[key] = deep_copy(value, memo)
        return new_dict
    
    # 其他类型暂时直接返回（可根据需要扩展）
    else:
        return obj


# 测试代码
def test_deep_copy():
    print("=== 测试深拷贝函数 ===")
    
    # 测试基本数据类型
    print("\n1. 测试基本数据类型:")
    test_int = 42
    test_str = "hello"
    test_bool = True
    test_none = None
    
    print(f"原始整数: {test_int}, 拷贝后: {deep_copy(test_int)}")
    print(f"原始字符串: {test_str}, 拷贝后: {deep_copy(test_str)}")
    print(f"原始布尔值: {test_bool}, 拷贝后: {deep_copy(test_bool)}")
    print(f"原始None: {test_none}, 拷贝后: {deep_copy(test_none)}")
    
    # 测试列表
    print("\n2. 测试列表:")
    test_list = [1, 2, [3, 4], "test"]
    copied_list = deep_copy(test_list)
    print(f"原始列表: {test_list}")
    print(f"拷贝后列表: {copied_list}")
    print(f"是否为同一对象: {test_list is copied_list}")
    print(f"嵌套列表是否为同一对象: {test_list[2] is copied_list[2]}")
    
    # 测试字典
    print("\n3. 测试字典:")
    test_dict = {"name": "Alice", "age": 20, "scores": {"math": 90, "english": 85}}
    copied_dict = deep_copy(test_dict)
    print(f"原始字典: {test_dict}")
    print(f"拷贝后字典: {copied_dict}")
    print(f"是否为同一对象: {test_dict is copied_dict}")
    print(f"嵌套字典是否为同一对象: {test_dict['scores'] is copied_dict['scores']}")
    
    # 测试循环引用
    print("\n4. 测试循环引用:")
    a = [1, 2]
    b = {"list": a}
    a.append(b)  # 创建循环引用: a -> b -> a
    
    try:
        copied_a = deep_copy(a)
        print("循环引用拷贝成功!")
        print(f"原始a的长度: {len(a)}")
        print(f"拷贝后a的长度: {len(copied_a)}")
        print(f"原始a[2] is b: {a[2] is b}")
        print(f"拷贝后copied_a[2] is copied_a[2]['list']: {copied_a[2]['list'] is copied_a}")
    except RecursionError:
        print("循环引用导致递归错误!")


if __name__ == "__main__":
    test_deep_copy()