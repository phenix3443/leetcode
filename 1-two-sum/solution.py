# -*- coding:utf-8; -*-
class Solution:
    def twoSum(self, nums, target):
        m = {v: i for i, v in enumerate(nums)}

        for i, v in enumerate(nums):
            l = m.get(target - v)
            if l and l != i:
                return [i, l]

        return
