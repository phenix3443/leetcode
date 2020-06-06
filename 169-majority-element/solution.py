# -*- coding:utf-8; -*-


class SolutionV1:
    """ 对所有数字排序，然后去nums[n/2]，时间复杂度O(nlogn)
    """

    def majorityElement(self, nums):
        nums.sort()
        mid = int(len(nums) / 2)
        return nums[mid]


class SolutionV2:
    """ 使用哈希表统计，时间复杂度O(n)，空间复杂度O(n)
    """

    def majorityElement(self, nums):
        static = {}
        majEle = nums[0]
        count = 1
        for n in nums:
            static[n] = static[n] + 1 if n in static else 1
            if static[n] > count:
                majEle = n
                count = static[n]

        return majEle


class Solution:
    """ 摩尔投票法
    """

    def majorityElement(self, nums):
        povit = nums[0]
        count = 1
        for i in nums[1:]:
            count += 1 if povit == i else -1
            if count == 0:
                povit = i
                count = 1

        return povit
