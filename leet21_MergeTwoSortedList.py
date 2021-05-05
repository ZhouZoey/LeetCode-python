# 合并两个有序的 链表
# 方法一： 递归
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution1(object):
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

class Solution2(object):
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        prehead = ListNode(-1)
        prev = prehead

        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        # 合并后，l1和l2最多还有一个元素未合并，直接放在结尾即可
        prev.next = l1 if l1 is not None else l2

        return prehead.next

if __name__ == "__main__":
    # 定义l1链表
    l1 = ListNode(2)
    l1.next = l11 = ListNode(4)
    l11.next = l12 = ListNode(5)
    # 定义l2链表
    l2 = ListNode(3)
    l2.next = l21 = ListNode(6)
    l21.next = l22 = ListNode(7)

    s = Solution2()
    res = s.mergeTwoLists(l1, l2)
    while res:
        print(res.val)
        res = res.next