"""
题目1：使用递归实现斐波那契数列 (Fibonacci)
使用递归函数完成斐波那契数列计算。
数列：1, 1, 2, 3, 5, 8, 13...（每一项等于前两项之和）。
逻辑：F(n) = F(n-1) + F(n-2)
出口：当 n 是 1 或 2 时，返回 1。
"""
from itertools import count


def fibonacci(n):
    if n <= 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

"""
题目2：使用递归解决汉诺塔问题 (Tower of Hanoi)
有三根柱子，要把一堆盘子从 A 移到 C，大盘子不能压在小盘子上。
逻辑：把上面 n-1 个盘子从 A 移到 B。把最底下的盘子从 A 移到 C。把 B 上的 n-1 个盘子移到 C。
"""
A = []  #原来
B = []  #辅助
C = []  #最终
counts = 0
def tower_of_hanoi(n, Y, Z, F,Y_name, Z_name, F_name):
    """

    :param n:
    :param Y:
    :param Z:
    :param F:
    :param Y_name:
    :param Z_name:
    :param F_name:
    :return:
    """
    global counts
    counts +=1
    print(counts)
    if n == 1:
        plant_num = Y.pop()
        Z.append(plant_num)
        print(Y_name,"=>",Z_name,plant_num)
        print(f"{Y_name}:{Y},{Z_name}:{Z},{F_name}:{F}")
        return
    tower_of_hanoi(n-1,Y, F, Z, Y_name, F_name, Z_name)
    plant_num = Y.pop()
    Z.append(plant_num)
    print(Y_name, "=>", Z_name, plant_num)
    print(f"{Y_name}:{Y},{Z_name}:{Z},{F_name}:{F}")
    tower_of_hanoi(n - 1, F, Z, Y, F_name, Z_name, Y_name)

"""
下面是地区字典，每个地区有subs子地区，当没有subs则表示它是最小的地区。输入一个地区的区号，查询对应的地区名称
例如输入：130910 
输出：吴桥县
"""
districts = {
    "name": "中国",
    "code": 86,
    "subs": [
        {"name": "北京", "code": 110},
        {"name": "天津", "code": 120},
        {"name": "河北", "code": 130, "subs": [
             {"name": "石家庄", "code": 1301},
             {"name": "唐山", "code": 1302},
             {"name": "秦皇岛", "code": 1303},
             {"name": "邯郸", "code": 1304},
             {"name": "邢台", "code": 1305},
             {"name": "保定", "code": 1306},
             {"name": "张家口", "code": 1307},
             {"name": "承德", "code": 1308},
             {"name": "沧州", "code": 1309, "subs": [
                  {"name": "新华区", "code": 130901},
                  {"name": "运河区", "code": 130902},
                  {"name": "泊头市", "code": 130903},
                  {"name": "黄骅市", "code": 130904},
                  {"name": "沧县", "code": 130905},
                  {"name": "青县", "code": 130906},
                  {"name": "沧县", "code": 130907},
                  {"name": "东光县", "code": 130908},
                  {"name": "肃宁县", "code": 130909},
                  {"name": "吴桥县", "code": 130910},
                  {"name": "献县", "code": 130911}
              ]}
          ]}
    ]}
def find_place(p_code,p_dist):
    for i in range(0,len(p_dist)):
        if p_dist[i]["code"] == p_code:
            return p_dist[i]["name"]
        else:
            if p_dist[i].get("subs") is not None:
                return find_place(p_code,p_dist[i]["subs"])


"""
编写一个名为 smart_stats 的函数，要求：
参数设计：接受一个必选参数 data（列表类型），以及一个可选的命名关键字参数 mode（默认值为 "mean"）。
功能实现：
若 mode="mean"，返回列表数据的平均值。
若 mode="max"，返回最大值。
若 mode="min"，返回最小值。
要求：使用函数注解标明参数和返回值的预期类型。
"""


def smart_stats(data, mode="mean"):
    def mean_stats(data):
        return sum(data) / len(data)
    def max_stats(data):
        return max(data)
    def min_stats(data):
        return min(data)

    if mode == "mean":
        return mean_stats(data)
    elif mode == "max":
        return max_stats(data)
    elif mode == "min":
        return min_stats(data)



if __name__ == '__main__':

    """ 
    n = int(input("斐波那契数列n"))
    for i in range(1,n):
    print(fibonacci(i))
    """

    """
    n = int(input("盘子个数n:"))
    A = [i for i in range(n,0,-1)]
    tower_of_hanoi(n, A, C, B,'A','C','B')
    """
    """
    code = int(input("输入地方号:"))
    print(find_place(code,districts["subs"]))

    """
    a_list = [1, 2, 3, 4]
    print(smart_stats(a_list, "min"))


