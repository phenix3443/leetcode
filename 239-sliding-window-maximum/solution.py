from typing import List
import heapq


class Solution:
    def maxSlidingWindowWithPriorityQueue(self, nums: List[int], k: int) -> List[int]:
        """
        暴力求解，每次都求k个数中的最大值，时间复杂度O(k),该操作需要执行n-k次，总体复杂度O(n^2)
        leetcode 运行超时
        """
        res = []
        for i in range(len(nums) - k + 1):
            res.append(heapq.nlargest(1, nums[i : i + k])[0])
        return res

    def maxSlidingWindowWithDQueue(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        window, res = [], []
        for i, v in enumerate(nums):
            if i >= k and window[0] <= i - k:
                window.pop(0)
            while window and nums[window[-1]] < v:  # 关键步骤
                window.pop()
            window.append(i)
            if i >= k - 1:
                res.append(nums[window[0]])
        return res
