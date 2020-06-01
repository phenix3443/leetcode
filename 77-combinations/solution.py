# -*- coding:utf-8; -*-


class Solution:
    def combine(self, n, k):
        result = []

        def helper(n, k, l):
            if len(l) == k:
                result.append(l)
                return

        return result
