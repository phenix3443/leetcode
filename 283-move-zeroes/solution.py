# -*- coding:utf-8; -*-
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zeroStart = 0
        for i in range(len(nums)):
            if nums[i]:  # 这里不使用num[i]!=0居然能加快速度
                if zeroStart != i:  # 避免原地互换
                    nums[zeroStart], nums[i] = nums[i], nums[zeroStart]
                zeroStart += 1
