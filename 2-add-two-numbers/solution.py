from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """两数相加"""
        head = ListNode(0)  # 哨兵节点
        l3 = head

        carry = 0  # 表示进位

        while l1 or l2:  # 这里设置比较巧妙
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            r = x + y + carry
            carry = r // 10  # 这个运算符比较巧妙

            l3.next = ListNode(r % 10)

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            l3 = l3.next  # 不要忘记这里

        if carry:
            l3.next = ListNode(1)

        return head.next
