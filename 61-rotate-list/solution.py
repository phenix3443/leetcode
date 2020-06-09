# -*- coding:utf-8; -*-


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    """

    def rotateRight(self, head, k):
        if not head:
            return head

        curr, count = head, 1

        while curr.next:
            count += 1
            curr = curr.next

        curr.next = head

        k = (count - k) % count  # 移动k次以后链表第一个元素

        while k > 0:  # 注意这里是等于，已经移动[1,k]个元素
            curr = head
            head = head.next
            k -= 1

        curr.next = None

        return head
