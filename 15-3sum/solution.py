from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = set()
        nums.sort()  # 排序后方便two-sum夹逼
        for i, v in enumerate(nums[:-2]):
            if i > 0 and nums[i] == nums[i - 1]:  # skip same
                continue
            d = {}
            for x in nums[i + 1 :]:
                if x not in d:
                    d[-x - v] = 1
                else:
                    ret.add((v, x, -v - x))
        return list(ret)
