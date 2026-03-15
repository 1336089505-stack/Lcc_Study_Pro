"""
1.	编写一个函数，实现二叉树节点的定义，并实现一个函数create_tree_from_list，
该函数接收一个按照层序遍历顺序给出的列表（其中用None表示空节点），构建一棵二叉树，并返回根节点。
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 实现从层序列表构建二叉树的函数
def create_tree_from_list(nodes_list):
    if not nodes_list:
        return None

    if nodes_list[0] is None:
        return None

    root = TreeNode(nodes_list[0])
    queue = deque([root])
    index = 1

    while queue and index < len(nodes_list):
        current_node = queue.popleft()

        left_val = nodes_list[index]
        if left_val is not None:
            current_node.left = TreeNode(left_val)
            queue.append(current_node.left)
        index += 1

        if index >= len(nodes_list):
            break
        right_val = nodes_list[index]
        if right_val is not None:
            current_node.right = TreeNode(right_val)
            queue.append(current_node.right)
        index += 1

    return root

"""
2.	编写一个函数max_depth，接收二叉树的根节点，
计算并返回二叉树的最大深度（根节点深度为1）。
要求使用递归方式实现。
"""
def max_depth(node):
    if node is None:
        return None
    if node.left is None and node.right is None:
        return 0
    return max(max_depth(node.left), max_depth(node.right)) + 1


"""
3.	编写一个函数inorder_traversal，接收二叉树的根节点，
返回二叉树中序遍历结果的列表。要求使用非递归方式实现（借助栈）
"""
def inorder_traversal(node):
    result = []  # 存储遍历结果
    stack = []  # 辅助栈，用于暂存节点
    curr = node  # 遍历指针，初始指向根节点W

    # 循环条件：指针未到空节点 或 栈不为空（还有未处理的节点）
    while curr is not None or stack:
        # 第一步：遍历到当前子树的最左节点，路径上的节点全部入栈
        while curr is not None:
            stack.append(curr)  # 节点入栈（暂存，后续访问）
            curr = curr.left  # 移动到左子节点

        # 第二步：弹出栈顶节点（最左节点/无左子的节点），访问它
        curr = stack.pop()
        result.append(curr.val)  # 将节点值加入结果列表

        # 第三步：处理该节点的右子树
        curr = curr.right

    return result

"""
4.	编写一个函数level_order_traversal，接收二叉树的根节点，
返回二叉树的层序遍历结果，要求结果以二维列表的形式组织，每一层单独为一个列表。
"""
def level_order_traversal(node):
    if root is None:
        return []

    result = []  # 最终的二维结果列表
    queue = deque([root])  # 队列存储待处理的节点，初始放入根节点

    # 队列不为空时循环（还有未处理的节点）
    while queue:
        level_size = len(queue)  # 关键：当前层的节点数量（队列长度）
        current_level = []  # 存储当前层的节点值

        # 遍历当前层的所有节点
        for _ in range(level_size):
            current_node = queue.popleft()  # 取出队列头部节点
            current_level.append(current_node.val)  # 记录当前节点值

            # 将当前节点的左、右子节点入队（下一层的节点）
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)

        # 当前层遍历完成，将该层结果加入最终列表
        result.append(current_level)

    return result

"""
5.	编写一个函数is_symmetric，接收二叉树的根节点，判断该二叉树是否是对称的（即镜像对称）。
"""
def is_symmetric(root):
    if root is None:
        return True
    return is_symmetric(root.left) and is_symmetric(root.right)


"""
6.	编写一个函数invert_tree，接收二叉树的根节点，翻转二叉树，
并返回翻转后的根节点。要求分别用递归方式和迭代方式（层序遍历）实现。
"""
def invert_tree_recursive(root):
    """
    递归方式翻转二叉树
    :param root: 二叉树的根节点
    :return: 翻转后的根节点
    """
    # 递归终止条件：节点为空，直接返回None
    if root is None:
        return None

    # 1. 递归翻转左子树和右子树
    left_subtree = invert_tree_recursive(root.left)
    right_subtree = invert_tree_recursive(root.right)

    # 2. 互换当前节点的左右子节点
    root.left = right_subtree
    root.right = left_subtree

    # 3. 返回当前节点（作为上层节点的子节点）
    return root


# ------------------- 迭代方式（层序遍历）实现翻转二叉树 -------------------
def invert_tree_iterative(root):
    """
    迭代方式（层序遍历）翻转二叉树
    :param root: 二叉树的根节点
    :return: 翻转后的根节点
    """
    # 边界情况：空树直接返回None
    if root is None:
        return None

    # 初始化队列，放入根节点（层序遍历的核心）
    queue = deque([root])

    while queue:
        # 取出当前层的节点
        current_node = queue.popleft()

        # 核心操作：互换当前节点的左右子节点
        current_node.left, current_node.right = current_node.right, current_node.left

        # 将非空的左、右子节点入队，继续处理下一层
        if current_node.left is not None:
            queue.append(current_node.left)
        if current_node.right is not None:
            queue.append(current_node.right)

    # 翻转后根节点不变，返回根节点
    return root




