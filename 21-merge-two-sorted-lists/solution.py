from typing import Optional
import unittest


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


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


class TestMergeTwoLists(unittest.TestCase):
    def test_mergeTwoLists(self):
        want = ListNode(
            1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4)))))
        )
        target = Solution().mergeTwoLists(
            ListNode(1, ListNode(2, ListNode(4))),
            ListNode(1, ListNode(3, ListNode(4))),
        )
        while want:
            self.assertEqual(want.val, target.val)
            want, target = want.next, target.next


if __name__ == "__main__":
    unittest.main()
