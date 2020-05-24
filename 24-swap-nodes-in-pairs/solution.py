# -*- coding:utf-8; -*-


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head):
        preHead = ListNode(-1)
        preHead.next = head  # 这里新增一个节点是因为头指针不会随着遍历一直到最后

        pre = preHead  # 假设pre是替换好的最后一个节点，那么只需要交换current(pre.next)和next(pre.next.next)即可
        while pre.next and pre.next.next:  # 只需要交换curr和follow即可
            c, n = pre.next, pre.next.next
            c.next, n.next = n.next, c  # 交换current和next
            pre.next = n
            pre = c  # 遍历前移

        return preHead.next
