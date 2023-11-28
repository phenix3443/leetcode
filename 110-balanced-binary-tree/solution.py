from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """平衡二叉树"""

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        if not (self.isBalanced(root.left) and self.isBalanced(root.right)):
            return False

        left = self.depth(root.left)

        right = self.depth(root.right)

        return abs(right - left) < 2

    def depth(self, node):
        if not node:
            return 0
        return 1 + max(self.depth(node.left), self.depth(node.right))
