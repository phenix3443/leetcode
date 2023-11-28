from typing import Optional, List
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """二叉树的中序遍历"""

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """递归思路"""
        res = []

        def helper(root):
            if not root:
                return
            helper(root.left)
            res.append(root.val)
            helper(root.right)

        helper(root)
        return res

    def inorderTraversalV2(self, root: Optional[TreeNode]) -> List[int]:
        """使用栈进行模拟递归"""
        res, stack, curr = [], [], root

        while stack or curr:
            while curr:
                stack.append(curr)  # 这里存储的是节点
                curr = curr.left

            top = stack.pop()  # 左子树已经遍历完成
            res.append(top.val)  # 处理
            curr = top.right

        return res


class TestInorderTraversal(unittest.TestCase):
    def test_inorderTraversal(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)
        self.assertEqual(Solution().inorderTraversal(root), [1, 3, 2])


if __name__ == "__main__":
    unittest.main()
