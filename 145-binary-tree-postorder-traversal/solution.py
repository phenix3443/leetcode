from typing import Optional, List
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """二叉树的后续遍历"""

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """递归解法"""
        res = []

        def helper(node):
            if not node:
                return
            helper(node.left)
            helper(node.right)
            res.append(node.val)

        helper(root)
        return res

    def postorderTraversalV2(self, root: Optional[TreeNode]) -> List[int]:
        """修改前序遍历规则，父->右->左，然后得出的结果做一下逆序"""
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


class TestPostorderTraversal(unittest.TestCase):
    def test_1(self):
        node1 = TreeNode(1)
        node2 = TreeNode(2)
        node3 = TreeNode(3)
        node1.right = node2
        node2.left = node3
        target = Solution().postorderTraversal(node1)
        self.assertEqual(target, [3, 2, 1])


if __name__ == "__main__":
    unittest.main()
