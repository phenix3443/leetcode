from typing import List
import unittest


class Solution:
    """组合总和二，这个代码还有问题"""

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = set()

        def helper(nums: List[int], nextCandidates: List[int]):
            if nextCandidates is None:
                return
            if sum(nums) == target:
                result.add(tuple(sorted(nums)))
                return
            if sum(nums) > target:
                return
            for i, v in enumerate(nextCandidates):
                helper(nums + [v], nextCandidates[i + 1 :])

        helper([], candidates)

        return [list(nums) for nums in result]


class TestCombinationSum(unittest.TestCase):
    def test_combination_sum(self):
        want = Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
        target = [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
        self.assertEqual(len(want), len(target))
        for v in target:
            self.assertIn(v, want)


if __name__ == "__main__":
    unittest.main()
