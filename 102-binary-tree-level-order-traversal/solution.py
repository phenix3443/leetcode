# -*- coding:utf-8; -*-
class Solution:
    """ 队列处理
    https://leetcode-cn.com/problems/binary-tree-level-order-traversal/solution/pythonicde-ji-jian-dai-ma-xie-fa-wu-xu-di-gui-wu-x/
    """

    def levelOrder(self, root):
        res = []
        currLevel = [(root,)]  # 这里处理比较巧妙
        while currLevel:  # 每次处理不是单个node，而是整个列表
            res.append([node.val for lrPairs in currLevel for node in lrPairs if node])
            currLevel = [
                (n.left, n.right) for lrPairs in currLevel for n in lrPairs if n
            ]

        return res[:-1]  # 因为最后一层的左右儿子都是null
