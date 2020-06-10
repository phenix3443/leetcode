# -*- coding:utf-8; -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class SolutionV1:
    """ 递归思路
    """

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


class Solution:
    """ 使用栈进行模拟递归
    """

    def inorderTraversal(self, root):
        res, stack, curr = [], [], root

        while stack or curr:
            while curr:
                stack.append(curr)  # 这里存储的是节点
                curr = curr.left

            top = stack.pop()  # 左子树已经遍历完成
            res.append(top.val)  # 处理
            curr = top.right

        return res
