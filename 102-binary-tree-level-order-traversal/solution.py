from typing import Optional, List
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
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
            res.append([node.val for lrPairs in currLevel for node in lrPairs if node])
            currLevel = [
                (node.left, node.right)
                for lrPairs in currLevel
                for node in lrPairs
                if node
            ]

        return res[:-1]  # 因为最后一层的左右儿子都是null
