# -*- coding:utf-8; -*-


class Solution:
    def maxArea(self, height: List[int]) -> int:
        m, l, r = 0, 0, len(height) - 1

        while l < r:
            minHeight = min(height[l], height[r])
            area = (r - l) * minHeight
            m = max(m, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return m
