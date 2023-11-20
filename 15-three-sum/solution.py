from typing import List


class Solution:
    """三数之和"""

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """转化为两数之和问题"""
        ret = set()
        nums.sort()  # 排序后方便去重
        for i, v in enumerate(nums[:-2]):
            if i > 0 and nums[i] == nums[i - 1]:  # skip same
                continue
            m = {}
            for x in nums[i + 1 :]:
                if -x - v not in m:  # 如果配对元素没有找到
                    m[x] = 1
                else:
                    ret.add((v, x, -v - x))
        return list(ret)
