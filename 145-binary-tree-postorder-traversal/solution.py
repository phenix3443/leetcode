# -*- coding:utf-8; -*-
class SolutionV2:
    """递归解法
    """

    def postorderTraversal(self, root):
        res = []

        def helper(root):
            if not root:
                return
            helper(root.left)
            helper(root.right)
            res.append(root.val)

        helper(root)
        return res


class Solution:
    """ 修改前序遍历规则，父->右->左，然后得出的结果做一下逆序

    """

    def postorderTraversal(self, root):
        res, stack, curr = [], [], root
        while stack or curr:
            while curr:
                res.append(curr.val)
                stack.append(curr)
                curr = curr.right
            top = stack.pop()
            curr = top.left

        res.reverse()
        return res
