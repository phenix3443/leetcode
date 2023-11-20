from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """合并两个有序链表"""

    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = ListNode(-1)
        p1, p2, p3 = list1, list2, head

        while p1 and p2:
            if p1.val <= p2.val:
                p3.next = p1
                p1 = p1.next
            else:
                p3.next = p2
                p2 = p2.next

            p3 = p3.next  # 不要忘记

        p3.next = p1 if p1 else p2

        return head.next
