# -*- coding:utf-8; -*-
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


class Solution:
    def compareTwoNode(self, p, q):
        if p == None and q == None:  # 两个都不存在
            return True

        if p == None or q == None:  # 只有一个存在
            return False

        if p.val != q.val:  # 两个都存在，但是值不相等
            return False

        left = self.compareTwoNode(p.left, q.right)

        right = self.compareTwoNode(p.right, q.left)

        return left and right

    def isSymmetric(self, root):
        if not root:
            return True

        return self.compareTwoNode(root.left, root.right)
