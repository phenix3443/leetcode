# -*- coding:utf-8; -*-

import math


class Solution:
    def depth(self, node):
        if not node:
            return 0
        return 1 + max(self.depth(node.left), self.depth(node.right))

    def isBalanced(self, root):
        if not root:
            return True

        if not (self.isBalanced(root.left) and self.isBalanced(root.right)):
            return False

        left = self.depth(root.left)

        right = self.depth(root.right)

        return abs(right - left) < 2
