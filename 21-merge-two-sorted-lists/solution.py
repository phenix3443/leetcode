# -*- coding:utf-8; -*-


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """迭代算法
        """
        head = ListNode(-1)
        p1 = l1
        p2 = l2
        p3 = head

        while p1 and p2:
            if p1.val <= p2.val:
                p3.next = p1
                p1 = p1.next
            else:
                p3.next = p2
                p2 = p2.next

            p3 = p3.next

        p3.next = p1 if p1 else p2

        return head.next
