from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionV1:
    """递归思路"""

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def helper(root):
            if not root:
                return
            helper(root.left)
            res.append(root.val)
            helper(root.right)

        helper(root)
        return res


class Solution:
    """使用栈进行模拟递归"""

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res, stack, curr = [], [], root

        while stack or curr:
            while curr:
                stack.append(curr)  # 这里存储的是节点
                curr = curr.left

            top = stack.pop()  # 左子树已经遍历完成
            res.append(top.val)  # 处理
            curr = top.right

        return res
