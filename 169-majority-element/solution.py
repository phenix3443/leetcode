from typing import List


class Solution:
    """多数元素"""

    def majorityElement(self, nums: List[int]) -> int:
        """排序后的中位数，时间复杂度O(nlogn)，空间复杂度O(1)"""
        nums.sort()
        mid = int(len(nums) / 2)
        return nums[mid]

    def majorityElementV2(self, nums):
        """使用哈希表统计，时间复杂度O(n)，空间复杂度O(n)"""
        m = {}
        target, count = nums[0], 1
        for n in nums:
            m[n] = m[n] + 1 if n in m else 1
            if m[n] > count:
                target, count = n, m[n]
        return target

    def majorityElementV3(self, nums):
        """摩尔投票法"""
        target, count = nums[0], 1
        for n in nums[1:]:
            count += 1 if target == n else -1
            if count == 0:
                target, count = n, 1
        return target
