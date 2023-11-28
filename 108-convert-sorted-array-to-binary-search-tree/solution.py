from typing import List, Optional

import math
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """将有序数组转换为二叉搜索树"""

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return
        mid = math.floor(len(nums) / 2)
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[0:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1 : len(nums)])

        return root


class TestSortedArrayToBST(unittest.TestCase):
    def compareTwoNode(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:  # 两个都不存在
            return True

        if p is None or q is None:  # 只有一个存在
            return False

        if p.val != q.val:  # 两个都存在，但是值不相等
            return False

        left = self.compareTwoNode(p.left, q.left)

        right = self.compareTwoNode(p.right, q.right)

        return left and right

    def test_1(self):
        node1 = TreeNode(0)
        node2 = TreeNode(-3)
        node3 = TreeNode(9)
        node4 = TreeNode(-10)
        node5 = TreeNode(5)
        node1.left = node2
        node1.right = node3
        node2.left = node4
        node3.left = node5
        target = Solution().sortedArrayToBST([-10, -3, 0, 5, 9])
        self.assertTrue(self.compareTwoNode(target, node1))


if __name__ == "__main__":
    unittest.main()
