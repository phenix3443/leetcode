from typing import Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """二叉树的最大深度"""

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


class TestMaxDepth(unittest.TestCase):
    def test_1(self):
        node1 = TreeNode(1)
        node2 = TreeNode(2)
        node3 = TreeNode(2)
        node4 = TreeNode(3)
        node5 = TreeNode(4)
        node6 = TreeNode(4)
        node7 = TreeNode(3)

        node1.left = node2
        node1.right = node3
        node2.left = node4
        node2.right = node5
        node3.left = node6
        node3.right = node7

        self.assertEqual(Solution().maxDepth(node1), 3)


if __name__ == "__main__":
    unittest.main()
