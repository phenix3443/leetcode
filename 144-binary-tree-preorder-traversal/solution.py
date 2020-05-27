# -*- coding:utf-8; -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root):
        res = []

        def helper(root):
            if not root:
                return []

            res.append(root.val)
            helper(root.left)
            helper(root.right)

        helper(root)
        return res
