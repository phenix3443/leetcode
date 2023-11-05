package solution

type ListNode struct {
	Val  int
	Next *ListNode
}

func swapPairs(head *ListNode) *ListNode {
	preHead := &ListNode{Next: head}
	pre := preHead
	for pre.Next != nil && pre.Next.Next != nil {
		a, b := pre.Next, pre.Next.Next
		pre.Next, a.Next, b.Next = b, b.Next, a
		pre = a
	}
	return preHead.Next
}
