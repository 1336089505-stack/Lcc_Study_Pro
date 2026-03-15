"""
1.	编写一个单向链表节点类 Node，包含属性 item 和 next。
然后编写链表类 LinkedList，
实现以下方法：is_empty()、length()、travel()（遍历打印）、
add(item)（头部添加）、append(item)（尾部添加）、
insert(pos, item)（指定位置添加）、remove(item)（删除第一个匹配的节点）、
search(item)（查找是否存在）。要求每个方法有注释，并考虑边界情况。
"""
class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def length(self):
        if self.is_empty():
            return 0
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def travel(self):
        if self.is_empty():
            print("链表为空，无数据可遍历")
            return
        current = self.head
        items = []
        while current is not None:
            items.append(str(current.item))
            current = current.next
        print("链表节点数据:"+"->".join(items))

    def add(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def append(self, item):
        new_node = Node(item)
        current = self.head
        while current is not None:
            if current.next is None:
                current.next = new_node
                break
            current = current.next

    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)
        else:
            new_node = Node(item)
            current = self.head
            count = 0
            while count < pos - 1:
                count += 1
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def remove(self, item):
        if self.is_empty():
            print("链表为空，无法删除节点")
            return
        current = self.head  # 当前遍历的节点
        pre = None  # 当前节点的前驱节点
        while current is not None:
            if current.item == item:
                if pre is None:
                    self.head = current.next
                    # 情况2：删除的是中间/尾节点
                else:
                    pre.next = current.next
                    # 找到第一个匹配项后立即退出，避免删除多个
                return
            pre = current
            current = current.next

    def search(self,item):
        if self.is_empty():
            return False
        current = self.head
        while current is not None:
            if current.item == item:
                return True
            current = current.next
        return False

"""
2.	编写一个栈类 Stack，使用列表实现，包含方法：push(item)、pop()、peek()、is_empty()、size()。
要求实现后进先出，pop和peek在栈空时返回None或引发异常（自行决定，但需注释说明）。
"""
class Stack():
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()
    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]
    def size(self):
        return len(self.items)

"""
3.	编写一个队列类 Queue，使用列表实现，包含方法：enqueue(item)、dequeue()、is_empty()、size()。
要求先进先出，dequeue在队列空时返回None。
"""
class Queue():
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop()
    def size(self):
        return len(self.items)

"""
4.	编写一个函数 binary_tree_depth(root)，计算二叉树的深度。假设二叉树节点类定义为：
class TreeNode:
def init(self, val):
self.val = val
self.left = None
self.right = None
函数返回树的深度（根节点深度为1）。要求递归实现。
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def binary_tree_depth(root):
    if root is None:
        return 0
    left_depth = binary_tree_depth(root.left)
    right_depth = binary_tree_depth(root.right)
    return 1 + max(left_depth, right_depth)

"""
5.	编写一个函数 reverse_linked_list(head)，反转一个单向链表。
给定头节点，返回新链表的头节点。
要求原地反转，不使用额外存储空间。
"""
def reverse_linked_list(head):
    if head is None or head.next is None:
        return head
    new_head = reverse_linked_list(head.next)
    head.next.next = head
    head.next = None
    return new_head

"""
6.	编写一个函数 is_balanced_parentheses(s)，
使用栈检查字符串s中的括号是否平衡。
括号包括圆括号()、方括号[]、花括号{}。
例如 "{[()]}" 返回True，"{[(])}" 返回False。
返回布尔值。
"""
def is_balanced_parentheses(s):
    bracket_map = {')': '(', ']': '[', '}': '{'}
    # 2. 初始化栈（用列表模拟，append入栈，pop出栈）
    stack = []

    # 3. 遍历字符串中的每个字符
    for char in s:
        # 忽略非括号字符（如果字符串包含其他字符，不影响括号检查）
        if char not in bracket_map and char not in bracket_map.values():
            continue

        # 4. 左括号：入栈
        if char in bracket_map.values():
            stack.append(char)
        # 5. 右括号：检查匹配
        else:
            # 栈为空（无左括号匹配）→ 不平衡
            if not stack:
                return False
            # 弹出栈顶元素，检查是否与当前右括号匹配
            top = stack.pop()
            if top != bracket_map[char]:
                return False

    # 6. 遍历结束后，栈必须为空（所有左括号都匹配完成）
    return len(stack) == 0



# 测试代码（可直接运行验证）
if __name__ == "__main__":
    # 创建链表实例
    ll = LinkedList()

    ll.add(5)
    ll.add(10)
    ll.add(10)
    ll.append(15)
    ll.append(20)
    ll.insert(3, 20)
    ll.remove(20)
    print(ll.search(20))
    ll.travel()
    # 测试空链表状态
    print("是否为空：", ll.is_empty())  # True
    print("链表长度：", ll.length())  # 0

