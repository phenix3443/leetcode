# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """ 思路：
    1. 任意一条路径均可以被看作由某个节点为起点，从其左儿子和右儿子向下遍历的路径（注意，不是节点）拼接得到。
    """

    maxDia = 0

    def dfs(self, root):
        if not root:
            return 0
        l = self.dfs(root.left)
        r = self.dfs(root.right)
        self.maxDia = max(self.maxDia, l + r)
        return max(l, r) + 1

    def diameterOfBinaryTree(self, root):
        self.dfs(root)
        return self.maxDia
