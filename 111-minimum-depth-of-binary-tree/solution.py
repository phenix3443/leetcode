# -*- coding:utf-8; -*-


class Solution:
    def minDepth(self, root):
        if not root:
            return 0

        if root.left == None or root.right == None:
            return 1 + self.minDepth(root.left or root.right)

        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
