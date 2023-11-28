from typing import List
import unittest


class Solution:
    """删除排序数组中的重复项"""

    def removeDuplicates(self, nums: List[int]) -> int:
        lastUniq = 0  # 前面唯一序列的最后一个元素
        for v in nums[1:]:
            if v != nums[lastUniq]:
                lastUniq += 1
                nums[lastUniq] = v

        return lastUniq + 1


class TestRemoveDuplicates(unittest.TestCase):
    def test_remove_duplicates(self):
        self.assertEqual(Solution().removeDuplicates([1, 1, 2]), 2)
        self.assertEqual(Solution().removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]), 5)


if __name__ == "__main__":
    unittest.main()
