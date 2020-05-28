# -*- coding:utf-8; -*-

import heapq


class Solution:
    def findKthLargest(self, nums, k):
        if len(nums) < k:
            return 0

        ret = heapq.nlargest(k, nums)

        return ret[-1]


if __name__ == "__main__":
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    s = Solution()
    print(s.findKthLargest(nums, k))
