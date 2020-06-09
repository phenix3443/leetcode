# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """递归思路：
    1. 分别在左子树和右子树中查找p,q，如果p,q分别位于左右子树中，那么当前节点就是公共节点

    """

    def lowestCommonAncestor(self, root, p, q):

        if root == None or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        elif left:
            return left
        else:
            return right
