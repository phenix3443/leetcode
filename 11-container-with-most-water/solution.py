from typing import List


class Solution:
    """盛最多水的容器"""

    def maxArea(self, height: List[int]) -> int:
        """
        相向双指针思路：
        1. 水的面积area=(r-l)*min(height[l],height[r])
        2. 如果是使用同向双指针的话，对于位置l，要把右边所有的元素遍历一遍。整体时间复杂度是O(n^2)。
        这是因为这种情况下，r-l是增大的，而且height[r]也是变化的。
        如果能将变化条件降低一维，有利于减少时间复杂度。
        考虑相向双指针，此时 (r-l)是缩小的，那么只有min(height[l],height[r])中的最小着替换为更大的值，水池面积才能增大。
        """
        m, l, r = 0, 0, len(height) - 1
        while l < r:
            area = (r - l) * min(height[l], height[r])
            m = max(m, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return m
