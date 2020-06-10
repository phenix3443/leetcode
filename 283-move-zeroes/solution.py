# -*- coding:utf-8; -*-
class Solution:
    def moveZeroes(self, nums):
        preZero = -1  # 指向遍历元素前面最后一个非0元素
        for i, v in enumerate(nums):
            if v != 0:
                preZero += 1
                if preZero != i:  # 避免原地互换
                    nums[preZero], nums[i] = nums[i], nums[preZero]


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    s = Solution()
    s.moveZeroes(nums)
    print(nums)
