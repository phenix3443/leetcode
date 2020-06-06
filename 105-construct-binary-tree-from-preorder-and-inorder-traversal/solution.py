# -*- coding:utf-8; -*-
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        if not inorder:
            return

        root = TreeNode(preorder[0])
        idx = inorder.index(root.val)
        # 因为不管在inorder还是preorder，idx+1前面都是root及其子树的节点
        root.left = self.buildTree(preorder[1 : idx + 1], inorder[:idx])
        root.right = self.buildTree(preorder[idx + 1 :], inorder[idx + 1 :])

        return root


if __name__ == "__main__":
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    s = Solution()
    s.buildTree(preorder, inorder)
