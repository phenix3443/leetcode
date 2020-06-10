# -*- coding:utf-8; -*-


class Solution:
    def removeDuplicates(self, nums):
        lastUniq = 0  # 前面唯一序列的最后一个元素
        for i, v in enumerate(nums[1:]):
            if v != nums[lastUniq]:
                lastUniq += 1
                nums[lastUniq] = v

        return lastUniq + 1
