# -*- coding:utf-8; -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head, k):
        preHead = ListNode(-1)
        preHead.next = head

        start, end, count = preHead, start.next, 0
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


if __name__ == "__main__":

    def printList(head):
        p = head
        while p:
            print(p.val)
            p = p.next

    nums = [1, 2, 3, 4, 5]
    head = ListNode(0)
    p = head
    for i in range(len(nums)):
        n = ListNode(nums[i])
        p.next = n
        p = n

    printList(head.next)

    s = Solution()
    printList(s.reverseKGroup(head.next, 2))
