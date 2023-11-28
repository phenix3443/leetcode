from typing import Optional
import unittest


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k):
        preHead = ListNode(-1)
        preHead.next = head

        start, count = preHead, 0
        end = start.next
        while end:
            count += 1
            if count % k == 0:  # 这里比较巧妙
                start = self.reverse(start, end.next)  # k个节点反转
                end = start.next  # 这里需要注意
            else:
                end = end.next

        return preHead.next

    def reverse(self, start, end):
        # (start,end）之间是可能要被反转的链表？为什么？因为要保证前后的联系
        first = start.next  # 保存将来反转后的最后一个元素，对接end
        pre, curr = start, start.next
        while curr != end:  # end对应单链表中的null
            tmp = curr.next
            curr.next = pre
            pre = curr
            curr = tmp

        start.next = pre
        first.next = curr

        return first  # 返回下一个start位置


class TestReverseKGroup(unittest.TestCase):
    def test_reverseKGroup(self):
        target = Solution().reverseKGroup(
            ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 3
        )
        want = ListNode(3, ListNode(2, ListNode(1, ListNode(4, ListNode(5)))))
        while target:
            self.assertEqual(target.val, want.val)
            target, want = target.next, want.next


if __name__ == "__main__":
    unittest.main()
