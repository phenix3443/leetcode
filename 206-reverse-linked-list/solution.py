# -*- coding:utf-8; -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head):
        pre, curr = None, head  # pre表示已经排好的
        while curr:
            tmp = curr.next
            curr.next = pre
            pre = curr
            curr = tmp

        return pre


if __name__ == "__main__":
    s = Solution()
