import unittest


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """二叉树前序遍历"""

    def preorderTraversal(self, root):
        res = []

        def helper(root):
            if not root:
                return
            res.append(root.val)
            helper(root.left)
            helper(root.right)

        helper(root)
        return res

    def preorderTraversalV2(self, root):
        res, stack, curr = [], [], root
        while stack or curr:
            while curr:
                res.append(curr.val)
                stack.append(curr)
                curr = curr.left
            top = stack.pop()
            curr = top.right
        return res


class TestPreorderTraversal(unittest.TestCase):
    def test_1(self):
        node1 = TreeNode(1)
        node2 = TreeNode(2)
        node3 = TreeNode(3)
        node1.right = node2
        node2.left = node3
        target = Solution().preorderTraversal(node1)
        self.assertEqual(target, [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
