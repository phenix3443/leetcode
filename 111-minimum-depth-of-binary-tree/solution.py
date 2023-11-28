from typing import Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """二叉树的最小深度"""

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if root.left is None or root.right is None:
            return 1 + self.minDepth(root.left or root.right)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))


class TestMinDepth(unittest.TestCase):
    def test_1(self):
        node1 = TreeNode(3)
        node2 = TreeNode(9)
        node3 = TreeNode(20)
        node4 = TreeNode(15)
        node5 = TreeNode(7)
        node1.left = node2
        node1.right = node3
        node3.left = node4
        node3.right = node5
        target = Solution().minDepth(node1)
        self.assertEqual(target, 2)


if __name__ == "__main__":
    unittest.main()
