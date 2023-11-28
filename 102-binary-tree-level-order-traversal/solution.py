from typing import Optional, List
import collections
import unittest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """二叉树的层序遍历"""

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = collections.deque()
        queue.append(root)
        while queue:
            level = []
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level:
                res.append(level)
        return res

    def levelOrder2(self, root: Optional[TreeNode]) -> List[List[int]]:
        """队列处理
        https://leetcode-cn.com/problems/binary-tree-level-order-traversal/solution/pythonicde-ji-jian-dai-ma-xie-fa-wu-xu-di-gui-wu-x/
        """
        res = []
        currLevel = [(root,)]  # 这里处理比较巧妙
        while currLevel:  # 每次处理不是单个node，而是整个列表
            res.append([n.val for lrPairs in currLevel for n in lrPairs if n])
            currLevel = [
                (n.left, n.right) for lrPairs in currLevel for n in lrPairs if n
            ]

        return res[:-1]  # 因为最后一层的左右儿子都是null


class TestLevelOrder(unittest.TestCase):
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

        self.assertEqual(Solution().levelOrder(node1), [[3], [9, 20], [15, 7]])


if __name__ == "__main__":
    unittest.main()
