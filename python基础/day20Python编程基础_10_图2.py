"""
1.	编写一个函数bfs_shortest_path(graph, start, end)，
使用广度优先搜索在无权无向图中找到从start到end的最短路径，
返回路径列表（包含起点和终点）。
如果不存在，返回None。graph用邻接表表示，
例如字典：{节点: [邻居]}。要求使用队列，并记录前驱。代码需有注释。
"""
from collections import deque


def bfs_shortest_path(graph, start, end):
    """
    使用BFS在无权无向图中找到从start到end的最短路径
    
    参数:
        graph: 邻接表表示的图，字典格式 {节点: [邻居]}
        start: 起点
        end: 终点
    
    返回:
        路径列表（包含起点和终点），如果不存在返回None
    """
    # 如果起点或终点不在图中，返回None
    if start not in graph and start != end:
        return None
    if start == end:
        return [start]
    
    # 队列用于BFS，存储当前访问的节点
    queue = deque([start])
    # 记录每个节点的前驱，用于最后重建路径
    predecessor = {start: None}
    # 记录已访问的节点
    visited = {start}
    
    # BFS循环
    while queue:
        # 从队列头部取出当前节点
        current = queue.popleft()
        
        # 遍历当前节点的所有邻居
        for neighbor in graph.get(current, []):
            # 如果邻居未被访问
            if neighbor not in visited:
                visited.add(neighbor)
                # 记录前驱
                predecessor[neighbor] = current
                
                # 找到目标节点
                if neighbor == end:
                    # 从终点回溯到起点，构建路径
                    path = []
                    node = end
                    while node is not None:
                        path.append(node)
                        node = predecessor[node]
                    return path[::-1]  # 反转得到从起点到终点的路径
                
                # 将邻居加入队列
                queue.append(neighbor)
    
    # 队列为空，说明不存在从start到end的路径
    return None
"""
2.	实现一个函数dijkstra(graph, start)，
使用Dijkstra算法计算从起点到所有其他节点的最短路径长度。
graph用邻接表表示，边权为正，例如：{节点: {邻居: 权重}}。
返回一个字典，键为节点，值为最短距离。要求使用优先队列（heapq）。注释。
"""
import heapq


def dijkstra(graph, start):
    """
    使用Dijkstra算法计算从起点到所有其他节点的最短路径长度
    
    参数:
        graph: 邻接表表示的带权图，字典格式 {节点: {邻居: 权重}}
        start: 起点
    
    返回:
        字典，键为节点，值为从起点到该节点的最短距离
    """
    # 初始化距离字典，所有节点距离设为无穷大
    distances = {node: float('inf') for node in graph}
    # 起点到自身的距离为0
    distances[start] = 0
    
    # 优先队列，存储 (距离, 节点) 元组
    # heapq是小顶堆，保证每次取出的是距离最小的节点
    priority_queue = [(0, start)]
    
    # 记录已确定最短距离的节点
    visited = set()
    
    # 主循环
    while priority_queue:
        # 取出距离最小的节点
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # 如果节点已确定最短距离，跳过
        if current_node in visited:
            continue
        
        # 标记为已访问
        visited.add(current_node)
        
        # 遍历当前节点的所有邻居
        for neighbor, weight in graph.get(current_node, {}).items():
            # 如果邻居未被确定最短距离
            if neighbor not in visited:
                # 计算从起点经过当前节点到邻居的距离
                new_distance = current_distance + weight
                
                # 如果新距离小于已知距离，则更新
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    # 将更新后的距离加入优先队列
                    heapq.heappush(priority_queue, (new_distance, neighbor))
    
    return distances


"""
3.	实现一个函数kahn_topological_sort(graph)，
使用Kahn算法对有向无环图进行拓扑排序。graph用邻接表表示，
返回一个列表，如果图有环则返回None。需要计算入度。注释。
"""
from collections import deque


def kahn_topological_sort(graph):
    """
    使用Kahn算法对有向无环图进行拓扑排序
    
    参数:
        graph: 邻接表表示的有向图，字典格式 {节点: [出边指向的节点]}
    
    返回:
        拓扑排序后的节点列表，如果图有环则返回None
    """
    # 计算每个节点的入度
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1
    
    # 将所有入度为0的节点加入队列（初始节点）
    queue = deque([node for node in graph if in_degree[node] == 0])
    
    # 拓扑排序结果
    result = []
    
    # BFS过程
    while queue:
        # 取出入度为0的节点
        node = queue.popleft()
        result.append(node)
        
        # 遍历该节点的所有邻居
        for neighbor in graph[node]:
            # 入度减1，相当于删除这条边
            in_degree[neighbor] -= 1
            # 如果邻居入度变为0，加入队列
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # 如果结果数量不等于节点数量，说明图中有环
    if len(result) != len(graph):
        return None
    
    return result

"""
4.	实现一个函数kruskal_mst(vertices, edges)，使用Kruskal算法求最小生成树。
vertices是顶点列表，edges是边列表，每个边为(u, v, weight)。
返回最小生成树的边列表，以及总权重。要求使用并查集。注释。
"""

class UnionFind:
    """
    并查集（Union-Find）数据结构
    用于 Kruskal 算法中检测是否形成环路
    """
    
    def __init__(self, vertices):
        # 每个节点的父节点初始化为自己
        self.parent = {v: v for v in vertices}
        # 每个节点的秩（用于优化合并）
        self.rank = {v: 0 for v in vertices}
    
    def find(self, x):
        """
        查找 x 所属集合的根节点（路径压缩）
        """
        if self.parent[x] != x:
            # 路径压缩：直接指向根节点
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        """
        合并 x 和 y 所在的集合（按秩合并）
        返回 True 如果合并成功，False 如果 x 和 y 已经在同一集合中
        """
        root_x = self.find(x)
        root_y = self.find(y)
        
        # 如果已经在同一集合中，不合并
        if root_x == root_y:
            return False
        
        # 按秩合并：秩小的合并到秩大的
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        
        return True


def kruskal_mst(vertices, edges):
    """
    使用Kruskal算法求最小生成树
    
    参数:
        vertices: 顶点列表
        edges: 边列表，每个元素为 (u, v, weight) 元组
    
    返回:
        (mst_edges, total_weight): 最小生成树的边列表和总权重
    """
    # 按权重从小到大排序所有边
    sorted_edges = sorted(edges, key=lambda x: x[2])
    
    # 初始化并查集
    uf = UnionFind(vertices)
    
    # 最小生成树的边列表
    mst_edges = []
    # 总权重
    total_weight = 0
    
    # 遍历排序后的边
    for u, v, weight in sorted_edges:
        # 如果 u 和 v 不在同一个集合中，则加入最小生成树
        if uf.union(u, v):
            mst_edges.append((u, v, weight))
            total_weight += weight
            
            # 最小生成树的边数达到 V-1 时停止
            if len(mst_edges) == len(vertices) - 1:
                break
    
    return mst_edges, total_weight

"""
5.	实现一个函数kosaraju_scc(graph)，
使用Kosaraju算法求有向图的强连通分量。
graph用邻接表表示，返回一个列表，
每个元素是一个强连通分量的顶点列表。需要两次DFS。注释。
"""
def kosaraju_scc(graph):
    """
    使用Kosaraju算法求有向图的强连通分量
    
    参数:
        graph: 邻接表表示的有向图，字典格式 {节点: [出边指向的节点]}
    
    返回:
        列表，每个元素是一个强连通分量的顶点列表
    """
    visited = set()
    finish_order = []
    
    # 第一次DFS：按后序遍历所有顶点，记录完成顺序
    def dfs_first(node):
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs_first(neighbor)
        # 节点遍历完成后，加入完成顺序列表
        finish_order.append(node)
    
    # 对所有未访问的节点进行第一次DFS
    for node in graph:
        if node not in visited:
            dfs_first(node)
    
    # 反转图
    reversed_graph = {node: [] for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            reversed_graph[neighbor].append(node)
    
    # 重置访问标记
    visited.clear()
    sccs = []
    
    # 第二次DFS：在反转图上，按完成时间的逆序进行遍历
    def dfs_second(node):
        component = []
        stack = [node]
        visited.add(node)
        
        while stack:
            current = stack.pop()
            component.append(current)
            
            for neighbor in reversed_graph.get(current, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
        
        return component
    
    # 按完成时间的逆序遍历
    for node in reversed(finish_order):
        if node not in visited:
            scc = dfs_second(node)
            sccs.append(scc)
    
    return sccs

"""
6.	实现一个函数warnsdorff_knight(n, start)，
使用Warnsdorff启发式规则在n×n棋盘上找一条骑士周游路径，
从start位置出发（start为元组(x,y)）。如果找到，返回路径列表；
否则返回None。注意启发式可能失败，需要处理回溯？
可以只实现启发式尝试，若失败返回None。注释。
"""

def warnsdorff_knight(n, start):
    """
    使用Warnsdorff启发式规则在n×n棋盘上找骑士周游路径
    
    参数:
        n: 棋盘大小 n×n
        start: 起始位置，元组 (x, y)，0 <= x, y < n
    
    返回:
        路径列表（包含所有访问的位置），如果找不到返回None
    """
    # 骑士的8个移动方向
    moves = [
        (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)
    ]
    
    def get_valid_moves(x, y, visited):
        """
        获取当前位置所有有效的下一步移动
        按照Warnsdorff启发式排序：优先选择出口最少的位置
        """
        valid = []
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            # 检查是否在棋盘内且未被访问
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                # 计算这个位置有多少个出口
                exit_count = 0
                for mdx, mdy in moves:
                    nx2, ny2 = nx + mdx, ny + mdy
                    if 0 <= nx2 < n and 0 <= ny2 < n and (nx2, ny2) not in visited:
                        exit_count += 1
                valid.append(((nx, ny), exit_count))
        
        # 按出口数量升序排序（Warnsdorff规则：选择出口最少的）
        valid.sort(key=lambda x: x[1])
        return [pos for pos, _ in valid]
    
    # 初始化
    visited = set()
    path = [start]
    visited.add(start)
    
    current = start
    
    # 贪心构建路径
    while len(path) < n * n:
        # 获取下一步可移动的位置（按Warnsdorff排序）
        next_moves = get_valid_moves(current[0], current[1], visited)
        
        # 如果没有可移动的位置
        if not next_moves:
            # 路径不完整，失败
            return None
        
        # 选择出口最少的位置（Warnsdorff启发式）
        next_pos = next_moves[0]
        
        # 移动到下一位置
        visited.add(next_pos)
        path.append(next_pos)
        current = next_pos
    
    # 成功走完所有格子
    return path


def print_board(n, path):
    """打印棋盘路径"""
    board = [[0] * n for _ in range(n)]
    for i, (x, y) in enumerate(path):
        board[y][x] = i + 1
    
    for row in board:
        print(' '.join(f'{val:3d}' for val in row))

if __name__ == '__main__':
    # 测试Dijkstra算法
    # 带权图：{节点: {邻居: 权重}}
    weighted_graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'A': 4, 'C': 1, 'D': 5},
        'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
        'D': {'B': 5, 'C': 8, 'E': 2},
        'E': {'C': 10, 'D': 2}
    }
    
    result = dijkstra(weighted_graph, 'A')
    print("从A到各节点的最短距离:", result)
    # 期望: {'A': 0, 'B': 3, 'C': 2, 'D': 8, 'E': 10}
    
    print("---")
    # 测试BFS
    graph_bfs = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'D'],
        'D': ['B', 'C', 'E'],
        'E': ['D']
    }
    print(bfs_shortest_path(graph_bfs, 'A', 'E'))  # ['A', 'D', 'E'] 或 ['A', 'C', 'D', 'E']
    
    # 测试用例2：不存在路径
    graph2 = {
        'A': ['B'],
        'B': ['A'],
        'C': ['D'],
        'D': ['C']
    }
    print(bfs_shortest_path(graph2, 'A', 'D'))  # None
    
    # 测试用例3：起点等于终点
    print(bfs_shortest_path(graph_bfs, 'A', 'A'))  # ['A']
    
    print("---")
    # 测试Kahn拓扑排序
    # 课程依赖图：A是基础课，B依赖A，C依赖A，D依赖B和C
    dag = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['D'],
        'D': []
    }
    print("DAG拓扑排序:", kahn_topological_sort(dag))
    
    # 有环的图
    graph_with_cycle = {
        'A': ['B'],
        'B': ['C'],
        'C': ['A']
    }
    print("有环图:", kahn_topological_sort(graph_with_cycle))
    
    print("---")
    # 测试Kruskal算法
    # 顶点列表
    vertices = ['A', 'B', 'C', 'D', 'E']
    # 边列表：(起点, 终点, 权重)
    edges = [
        ('A', 'B', 1),
        ('A', 'C', 3),
        ('B', 'C', 2),
        ('B', 'D', 4),
        ('C', 'D', 5),
        ('C', 'E', 6),
        ('D', 'E', 7)
    ]
    
    mst, total = kruskal_mst(vertices, edges)
    print("最小生成树的边:", mst)
    print("总权重:", total)
    
    print("---")
    # 测试Kosaraju算法 - 强连通分量
    # 有向图：A->B->C形成一个环，D单独一个节点
    scc_graph = {
        'A': ['B'],
        'B': ['C'],
        'C': ['A'],  # A、B、C形成强连通分量
        'D': []
    }
    print("强连通分量:", kosaraju_scc(scc_graph))
    
    print("---")
    # 测试Warnsdorff骑士周游算法
    # 5x5棋盘，从(0,0)开始
    path = warnsdorff_knight(5, (0, 0))
    if path:
        print(f"找到骑士周游路径，共{len(path)}步")
        print_board(5, path)
    else:
        print("未找到周游路径")
