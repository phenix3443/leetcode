from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """两数之和"""
        m = {}
        for i, v in enumerate(nums):
            if target - v in m:  # 如果配对元素在列表中
                return [m[target - v], i]
            m[v] = i
