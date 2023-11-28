from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """环形链表位置"""

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        双指针：fast每次走两步，slow每次走一步
        假设：head到环起点的长度为x，环起点到相遇点距离为y，相遇点到环起点距离为z
        fast走的路程总长为x+y+z+y
        slow走的路程总长为 x+y
        又因相同时间fast走的路程是slow的两倍，所以，2(x+y)=x+y+z+y，即x=z.
        所以当fast和slow相遇的时候，让其中一个指针从head开始遍历，然后另外一个指针同步继续往后走，那么，他们最终相遇的点就是环的起点。
        """
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if fast is slow:
                fast = head
                while fast is not slow:
                    fast, slow = fast.next, slow.next
                return fast
        return None
