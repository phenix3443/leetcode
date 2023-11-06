class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class SolutionV1:
    def preorderTraversal(self, root):
        res = []

        def helper(root):
            if not root:
                return
            res.append(root.val)
            helper(root.left)
            helper(root.right)

        helper(root)
        return res


class Solution:
    def preorderTraversal(self, root):
        res, stack, curr = [], [], root
        while stack or curr:
            while curr:
                res.append(curr.val)
                stack.append(curr)
                curr = curr.left
            top = stack.pop()
            curr = top.right
        return res
