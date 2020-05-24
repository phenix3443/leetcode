# -*- coding:utf-8; -*-
"""
双指针：fast每次走两步，slow每次走一步
假设：head到长度为x，环起点到相遇点距离为y，相遇点到环起点距离为z
fast走的路程总长为x+y+z+y
slow走的路程总长为 x+y
又因相同时间fast走的路程是slow的两倍，所以，2(x+y)=x+y+z+y，即x=z.
所以当fast和slow相遇的时候，让其中一个指针从head开始遍历，然后另外一个指针同步继续往后走，那么，他们最终相遇的点就是环的起点。
"""


class Solution:
    def hasCycle(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:  # 已经相遇
                fast = head
                pos = 1
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                    pos += 1
                else:
                    return pos + 1

        return -1
