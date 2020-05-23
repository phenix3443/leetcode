# -*- coding:utf-8; -*-


class Solution:
    def maxArea(self, height: List[int]) -> int:
        c = len(height)
        m = 0

        for l in range(c - 1):
            for r in range(l + 1, c):
                area = (r - l) * min(height[l], height[r])
                m = max(m, area)
        return m
