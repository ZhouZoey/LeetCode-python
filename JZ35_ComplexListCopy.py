# 复制链表
# 普通链表复制
class Node:
    def __init__(self, x: int, next: 'Node' = None):
        self.val = int(x)
        self.next = next

class Solution(object):
    def copyRandomList(self, head: 'Node') -> 'Node':
        cur = head
        dum = pre = Node[0]
        while cur:
            node = Node(cur.val)  # 复制结点
            pre.next = node       # 新链表的前驱结点-》当前结点
            cur = cur.next        # 遍历下一结点
            pre = node            # 保存当前新结点
        return dum.next

# 包含random指针的链表复制
class Node1:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

# 方法一：hash法
class Solution1(object):
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return
        dic = { }
        cur = head
        while cur:
            dic[cur] = Node(cur.val)
            cur = cur.next
        # 构建新结点的next和Random指向
        cur = head
        while cur:
            dic[cur].next = dic.get(cur.next)
            dic[cur].random = dic.get(cur.random)
            cur = cur.next
        return dic[head]

# 方法二：先拼接链表，再拆分
class Solution2(object):
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return
        cur = head
        # 1、复制各节点，拼接链表
        while cur:
            tmp = Node(cur.val)
            tmp.next = cur.next
            cur.next = tmp
            cur = tmp.next
        # 2、构建新结点的random指向
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        # 3 拆分两链表
        cur = res = head.next
        pre = head
        while cur.next:
            pre.next = pre.next.next
            cur.next = cur.next.next
            pre = pre.next
            cur = cur.next
        pre.next = None
        return res
