# -*- coding:utf-8; -*-
class Solution:
    def permute(self, nums):
        result = []

        def helper(i, nums, r):
            if i == len(nums):
                result.append(r)
                return

            for i in nums[i % len(nums)]:
                helper(i + 1, nums, r + [nums[i % len(nums)]])

        helper(0, nums, [0] * len(nums))
        return result
