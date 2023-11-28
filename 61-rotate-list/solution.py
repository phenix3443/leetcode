from typing import Optional
import unittest


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    """旋转列表"""

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        tail, count = head, 1

        # 计算链表长度,并将尾部连接到头部形成环
        while tail.next:
            count += 1
            tail = tail.next
        tail.next = head

        # 移动k次以后链表第一个元素,即为旋转后的第一个元素，注意这里的计算
        k = (count - k) % count

        while k > 0:  # 注意这里是等于，已经移动[1,k]个元素
            tail, head, k = head, head.next, k - 1

        tail.next = None

        return head


class TestRotateRight(unittest.TestCase):
    def test_1(self):
        target = Solution().rotateRight(
            ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2
        )
        want = ListNode(4, ListNode(5, ListNode(1, ListNode(2, ListNode(3)))))
        while target:
            self.assertEqual(target.val, want.val)
            target, want = target.next, want.next


if __name__ == "__main__":
    unittest.main()
