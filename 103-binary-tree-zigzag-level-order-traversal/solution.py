from typing import Optional, List
import unittest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """二叉树的锯齿形层序遍历"""

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """队列处理
        https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/solution/guan-fang-suan-fa-you-hua-pythonicji-jian-dai-ma-y/
        主要是利用python list遍历的特性，step
        """
        res = []
        currLevel = [(root,)]  # 这里处理比较巧妙
        step = 1
        while currLevel:  # 每次处理不是单个node，而是整个列表
            res.append(
                [n.val for lrPairs in currLevel[::step] for n in lrPairs[::step] if n]
            )
            step = -step
            currLevel = [
                (n.left, n.right) for lrPairs in currLevel for n in lrPairs if n
            ]

        return res[:-1]  # 因为最后一层的左右儿子都是null


class TestZigzagLevelOrder(unittest.TestCase):
    def test_1(self):
        node1 = TreeNode(3)
        node2 = TreeNode(9)
        node3 = TreeNode(20)
        node4 = TreeNode(15)
        node5 = TreeNode(7)

        node1.left = node2
        node1.right = node3
        node3.left = node4
        node3.right = node5

        self.assertEqual(Solution().zigzagLevelOrder(node1), [[3], [20, 9], [15, 7]])


if __name__ == "__main__":
    unittest.main()
