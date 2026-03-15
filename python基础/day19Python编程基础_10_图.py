"""
1.	实现一个函数 bfs_shortest_path(graph, start, end)，
使用广度优先搜索在无权图中找到从start到end的最短路径，返回路径列表。
如果不存在，返回None。图用邻接表表示，字典形式，键为顶点，值为邻居列表。要
求路径包含起点和终点
"""
from collections import deque


def bfs_shortest_path(graph, start, end):
    # 边界1：起点和终点相同，直接返回自身
    if start == end:
        return [start]

    # 边界2：起点/终点不在图中，直接返回None
    if start not in graph or end not in graph:
        return None

    # 1. 初始化队列：存储待遍历的节点，BFS核心结构
    queue = deque()
    queue.append(start)

    # 2. 初始化已访问集合：避免重复遍历（防止环、死循环）
    visited = set()
    visited.add(start)

    # 3. 初始化前驱字典：key=当前节点，value=前驱节点（用于回溯路径）
    parent = {}
    parent[start] = None  # 起点无前驱

    # 4. BFS核心遍历
    while queue:
        # 取出队首节点（FIFO，保证广度优先）
        current_node = queue.popleft()

        # 遍历当前节点的所有邻居
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                # 记录邻居的前驱节点
                parent[neighbor] = current_node
                # 标记为已访问
                visited.add(neighbor)
                # 邻居入队
                queue.append(neighbor)

                # 找到终点，提前终止遍历（最优解）
                if neighbor == end:
                    queue = deque()  # 清空队列，退出循环
                    break

    # 5. 回溯生成路径：从终点往起点找前驱
    path = []
    current = end
    while current is not None:
        path.append(current)
        # 终点不在前驱字典中，说明无路径
        if current not in parent:
            return None
        current = parent[current]

    # 反转路径（从起点→终点）
    path.reverse()
    return path

"""
2.	实现一个函数 dfs_recursive(graph, start)，
使用递归深度优先搜索遍历图，返回从start出发的访问顺序列表。
图用邻接表表示，假设图是无向图，但需要考虑避免重复访问。
"""
def dfs_recursive(graph, start):
    # 边界条件：起点不在图中，返回空列表
    if start not in graph:
        return []

    # 已访问集合：防止重复访问（无向图必备）
    visited = set()
    # 存储访问顺序
    result = []

    # 定义递归辅助函数
    def dfs(node):
        # 1. 标记当前节点为已访问
        visited.add(node)
        # 2. 将当前节点加入访问顺序列表
        result.append(node)

        # 3. 递归遍历所有未被访问的邻居节点
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    # 从起点开始递归遍历
    dfs(start)
    # 返回最终的访问顺序
    return result

"""
3.	实现一个函数 has_cycle_directed(graph)，
使用深度优先搜索判断有向图是否存在环。
图用邻接表表示，返回布尔值。需要利用递归栈标记
"""
def has_cycle_directed(graph):
    # 全局已访问的节点集合
    visited = set()
    # 递归栈：记录当前DFS路径上的节点（核心判环标记）
    rec_stack = set()

    def dfs(node):
        # 1. 当前节点加入 已访问集合 和 递归栈
        visited.add(node)
        rec_stack.add(node)

        # 2. 遍历所有邻接节点
        for neighbor in graph[node]:
            # 邻接节点未访问：递归遍历
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            # 邻接节点在递归栈中：找到环！
            elif neighbor in rec_stack:
                return True

        # 3. 回溯：当前节点遍历完成，移出递归栈
        rec_stack.remove(node)
        return False

    # 遍历图中所有节点（处理不连通的有向图）
    for node in graph:
        if node not in visited:
            if dfs(node):
                return True
    return False

"""
4.	实现一个函数 topological_sort_dfs(graph)，
使用深度优先搜索对有向无环图进行拓扑排序，
返回顶点列表。如果图有环，则返回None。
图用邻接表表示。
"""
def topological_sort_dfs(graph):
    # 定义节点状态：0=未访问，1=访问中(递归栈)，2=已访问完成
    state = {node: 0 for node in graph}
    # 存储后序遍历结果
    post_order = []
    # 标记是否存在环
    has_cycle = False

    def dfs(node):
        nonlocal has_cycle
        # 发现环：当前节点在递归栈中（访问中）
        if state[node] == 1:
            has_cycle = True
            return
        # 已访问完成，直接返回
        if state[node] == 2:
            return

        # 标记为【访问中】（进入递归栈）
        state[node] = 1
        # 递归遍历所有邻接节点
        for neighbor in graph[node]:
            dfs(neighbor)
            # 提前终止：发现环直接返回
            if has_cycle:
                return
        # 所有邻接节点遍历完成，标记为【已访问】
        state[node] = 2
        # 后序遍历：加入结果列表
        post_order.append(node)

    # 遍历所有节点（处理不连通的图）
    for node in graph:
        if state[node] == 0:
            dfs(node)
            # 有环直接返回None
            if has_cycle:
                return None

    # 后序遍历反转 → 拓扑排序
    return post_order[::-1]

"""
5.	实现一个函数 dfs_with_times(graph)，
对图进行深度优先搜索，记录每个顶点的发现时间和结束时间。
图可能不连通，需要遍历所有顶点。
返回两个字典：discovery和finish，键为顶点，值为整数时间戳（从1开始）
"""
def dfs_with_times(graph):
    # 存储发现时间：key=顶点, value=时间戳
    discovery = {}
    # 存储结束时间：key=顶点, value=时间戳
    finish = {}
    # 记录已访问节点
    visited = set()
    # 时间戳从1开始
    time = 1

    # 递归DFS核心函数
    def dfs(node):
        # 声明time为外部变量，允许修改
        nonlocal time

        # 1. 发现当前节点：标记访问、记录发现时间、时间+1
        visited.add(node)
        discovery[node] = time
        time += 1

        # 2. 递归遍历所有未访问的邻居节点
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

        # 3. 结束当前节点：所有子节点遍历完成，记录结束时间、时间+1
        finish[node] = time
        time += 1

    # 遍历所有顶点，处理【不连通图】（关键）
    for vertex in graph:
        if vertex not in visited:
            dfs(vertex)



"""
6.	实现一个函数 find_connected_components(graph)，
使用BFS或DFS找出无向图的所有连通分量，
返回一个列表，每个元素是一个连通分量的顶点列表。图用邻接表表示。
"""
from collections import deque

def find_connected_components(graph):
    visited = set()
    components = []
    
    def bfs(start):
        component = []
        queue = deque([start])
        visited.add(start)
        
        while queue:
            node = queue.popleft()
            component.append(node)
            
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return component
    
    for vertex in graph:
        if vertex not in visited:
            component = bfs(vertex)
            components.append(component)
    
    return components
