from typing import List


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
