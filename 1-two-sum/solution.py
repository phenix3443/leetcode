from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i, v in enumerate(nums):
            if target - v in m:
                return [m[target - v], i]
            m[v] = i
