from typing import List
import unittest


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


class TestThreeSum(unittest.TestCase):
    def test_1(self):
        nums = [-1, 0, 1, 2, -1, -4]
        r = Solution().threeSum(nums)
        for i in r:
            self.assertIn(sorted(i), [[-1, -1, 2], [-1, 0, 1]])


if __name__ == "__main__":
    unittest.main()
