# -*- coding:utf-8; -*-


class Solution:
    def combine(self, n, k):
        if k == 0:
            return []

        result = []

        def helper(k, l):
            if len(l) == k:
                result.append(l)
                return

            start = l[-1] + 1 if l else 1
            for m in range(start, n + 1):
                helper(k, l + [m])

        helper(k, [])

        return result
