from typing import List
import unittest


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """两数之和"""
        m = {}
        for i, v in enumerate(nums):
            if target - v in m:  # 如果配对元素在列表中
                return [m[target - v], i]
            m[v] = i


class TestTwoSum(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Solution().twoSum([2, 7, 11, 15], 9), [0, 1])


if __name__ == "__main__":
    unittest.main()
