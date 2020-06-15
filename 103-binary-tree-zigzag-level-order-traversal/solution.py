# -*- coding:utf-8; -*-
class Solution:
    """ 队列处理
    https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/solution/guan-fang-suan-fa-you-hua-pythonicji-jian-dai-ma-y/
    主要是利用python list遍历的特性，step
    """

    def zigzagLevelOrder(self, root):
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
