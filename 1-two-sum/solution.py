# -*- coding:utf-8; -*-
class Solution:
    def twoSum(self, nums, target):
        m = {nums[i]: i for i in range(len(nums))}

        for i in range(len(nums)):
            l = m.get(target - nums[i])
            if l and l != i:
                return [i, l]

        return
