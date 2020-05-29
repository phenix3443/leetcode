# -*- coding:utf-8; -*-
import heapq


class Solution:
    def maxSlidingWindow(self, nums, k):
        res = []
        for i in range(len(nums) - k + 1):
            h = [-e for e in nums[i : i + k]]
            heapq.heapify(h)
            res.append(-heapq.heappop(h))
        return res


if __name__ == "__main__":
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    s = Solution()
    print(s.maxSlidingWindow(nums, k))
