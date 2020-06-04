# -*- coding:utf-8; -*-
class SolutionV1:
    def permute(self, nums):
        result = []

        def helper(i, nums, r):
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
                helper(i + 1, nums, r)

            # 4. 清理当前层:当前层没有要清理的

        helper(0, nums, [])
        return result


class Solution:
    """ 从语言层面对代码进行优化
    """

    def permute(self, nums):
        result = []

        numsLen = len(nums)
        origNums = set(nums)

        def helper(i, nums, r):
            if i == numsLen:
                result.append(r)
                return

            for k in origNums - set(r):
                helper(i + 1, nums, r + [k])

        helper(0, nums, [])
        return result
