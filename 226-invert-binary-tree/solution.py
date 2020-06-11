# -*- coding:utf-8; -*-


class Solution:
    """
    解题思路：递归
    """

    def invertTree(self, root):
        if not root:
            return

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        return root
