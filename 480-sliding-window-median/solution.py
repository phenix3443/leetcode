from typing import List
import heapq


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        """
        leetcode 超时
        """
        window, res = [], []
        for i, v in enumerate(nums):
            if i >= k:
                window.remove(nums[i - k])
            window.append(nums[i])
            if i >= k - 1:
                window.sort()
                res.append(window[k // 2] / 2.0 + window[(k - 1) // 2] / 2.0)

        return res

    def medianSlidingWindowWithPriorityQueue(
        self, nums: List[int], k: int
    ) -> List[float]:
        """
        使用大小堆进行处理
        """
        for i, v in enumerate(nums):
            pass

        return None
