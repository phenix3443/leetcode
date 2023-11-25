from typing import List


class Solution:
    """全排列 2"""

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        与46题目类似，可将重复元素换成数组下标
        """
        result = []
        numsLen, origNums = len(nums), set([i for i in range(len(nums))])

        def helper(i, r):
            if i == numsLen:
                result.append(r)
                return

            for k in origNums - set(r):
                helper(i + 1, r + [k])

        helper(0, [])
        return list(set([tuple([nums[i] for i in idxs]) for idxs in result]))
