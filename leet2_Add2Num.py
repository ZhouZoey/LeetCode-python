# leetcode-3: Add two numbers
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 创建一个结点值为None的头结点
        dummy = p = ListNode(None)
        s = 0
        while l1 or l2 or s:
            s += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            p.next = ListNode(s % 10)  # 指向新链表
            p = p.next
            s //= 10   # 有进位则取模
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next # 因为dummy指向空结点，所以下一个结点才是新链表的头结点

if __name__ == '__main__':
    # 定义l1链表
    l1 = ListNode(2)
    l1.next = l11 = ListNode(4)
    l11.next = l12 = ListNode(5)
    # 定义l2链表
    l2 = ListNode(5)
    l2.next = l21 = ListNode(6)
    l21.next = l22 = ListNode(4)

    # 创建对象
    s = Solution()
    # 获取返回值链表
    res = s.addTwoNumbers(l1, l2)
    # 循环遍历读链表
    while res:
        print(res.val)
        res = res.next
