from typing import Optional
import unittest


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


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


class TestSwapPairs(unittest.TestCase):
    def test_swapPairs(self):
        target = Solution().swapPairs(
            ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
        )
        want = ListNode(2, ListNode(1, ListNode(4, ListNode(3))))
        while target:
            self.assertEqual(target.val, want.val)
            target, want = target.next, want.next


if __name__ == "__main__":
    unittest.main()
