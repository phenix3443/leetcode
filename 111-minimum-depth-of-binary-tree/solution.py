from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if root.left is None or root.right is None:
            return 1 + self.minDepth(root.left or root.right)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
