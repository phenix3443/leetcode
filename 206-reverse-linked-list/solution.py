# -*- coding:utf-8; -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class SolutionV1:
    def reverseList(self, head):
        pre, curr = None, head  # pre表示已经排好的
        while curr:
            tmp = curr.next
            curr.next = pre
            pre, curr = curr, tmp

        return pre


class Solution:
    """ 递归实现
    """

    def reverseList(self, head):
        if head == None or head.next == None:
            return head

        node = head
        head = self.reverseList(head.next)

        node.next.next = node
        node.next = None
        return head
