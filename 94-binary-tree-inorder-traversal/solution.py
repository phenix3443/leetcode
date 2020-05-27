# -*- coding:utf-8; -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root):
        res = []

        def helper(root):
            if not root:
                return []
            helper(root.left)
            res.append(root.val)
            helper(root.right)

        helper(root)
        return res
