from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """两两交换链表中的节点"""

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        preHead = ListNode(-1)
        preHead.next = head

        pre = preHead
        while pre.next and pre.next.next:
            a, b = pre.next, pre.next.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return preHead.next
