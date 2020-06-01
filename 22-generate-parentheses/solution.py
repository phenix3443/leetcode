# -*- coding:utf-8; -*-

"""
思路：将手写的方法转化为代码。

"""


class Solution:
    def generateParenthsis(self, n):
        result = []

        def helper(left, right, n, s):
            if left == n and right == n:
                result.append(s)
            if left < n:
                helper(left + 1, right, n, s + "(")
            if right < left:
                helper(left, right + 1, n, s + ")")

        helper(0, 0, n, "")
        return result
