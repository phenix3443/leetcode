# -*- coding:utf-8; -*-


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
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
