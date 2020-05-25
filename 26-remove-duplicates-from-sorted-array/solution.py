# -*- coding:utf-8; -*-


class Solution:
    def removeDuplicates(self, nums):
        lastUniq, i = 0, 0
        while i < len(nums) - 1:
            i += 1
            if nums[i] != nums[lastUniq]:
                lastUniq += 1
                nums[lastUniq] = nums[i]

        return lastUniq + 1
