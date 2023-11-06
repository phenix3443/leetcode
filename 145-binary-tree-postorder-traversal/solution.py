from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionV2:
    """递归解法"""

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def helper(node):
            if not node:
                return
            helper(node.left)
            helper(node.right)
            res.append(node.val)

        helper(root)
        return res


class Solution:
    """修改前序遍历规则，父->右->左，然后得出的结果做一下逆序"""

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
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
