from typing import List


class Solution:
    """跳跃游戏 II"""

    def jump(self, nums: List[int]) -> int:
        step = 0
        end = 0
        max_bound = 0
        for i, v in enumerate(nums):
            max_bound = max(max_bound, v + i)
            if i == end:
                step += 1
                end = max_bound
        return step
