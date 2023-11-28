from typing import Optional
import unittest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """对称二叉树"""

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        1. 划分子问题：该问题取决于左右子树是否对称。所以递归函数形式 func(left,right)->bool
        2. 分析left和right对称的定义，也就是func的实现：
        1. 如果left,right都不存在，那么肯定对称。
        2. 如果left,right只有一个存在，那么肯定不对称。
        3. 如果left,right都存在，但是值不相同，肯定不对称。
        4. 如果left,right都存在，值相同，left,right对称需要满足：
            1. left的左子树和right的右子树对称。
            2. left的右子树和right的左子树对称。
        可以看到，第四步就是递归的步骤。
        """
        if not root:
            return True

        return self.compareTwoNode(root.left, root.right)

    def compareTwoNode(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:  # 两个都不存在
            return True

        if p is None or q is None:  # 只有一个存在
            return False

        if p.val != q.val:  # 两个都存在，但是值不相等
            return False

        left = self.compareTwoNode(p.left, q.right)

        right = self.compareTwoNode(p.right, q.left)

        return left and right


class TestIsSymmetric(unittest.TestCase):
    def test_1(self):
        node1 = TreeNode(1)
        node2 = TreeNode(2)
        node3 = TreeNode(2)
        node4 = TreeNode(3)
        node5 = TreeNode(4)
        node6 = TreeNode(4)
        node7 = TreeNode(3)

        node1.left = node2
        node1.right = node3
        node2.left = node4
        node2.right = node5
        node3.left = node6
        node3.right = node7

        self.assertEqual(Solution().isSymmetric(node1), True)


if __name__ == "__main__":
    unittest.main()
