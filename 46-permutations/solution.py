from typing import List


class SolutionV1:
    """全排列"""

    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def helper(i, r):
            # 1. 终止条件
            if i == len(nums):
                result.append(r)
                return
            # 2. 处理当前逻辑
            newR = []
            for k in set(nums) - set(r):
                newR.append(r + [k])

            # 3. 下探递归
            for r in newR:
                helper(i + 1, r)

            # 4. 清理当前层:当前层没有要清理的

        helper(0, [])
        return result


class Solution:
    """从语言层面对代码进行优化"""

    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        numsLen, origNums = len(nums), set(nums)

        def helper(i, r):
            if i == numsLen:
                result.append(r)
                return

            for k in origNums - set(r):
                helper(i + 1, r + [k])

        helper(0, [])
        return result
