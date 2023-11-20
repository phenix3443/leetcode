from typing import List


class Solution:
    """组合总和"""

    def combinationSumV1(self, candidates: List[int], target: int) -> List[List[int]]:
        # 1. 定义保存结果的组合
        result = set()

        # 2. 定义递归函数，只有一个参数表示递归层数，在这里的参数i表示用于构成 target 的数字列表
        def helper(nums: List[int]):
            # 4. 编写递归模板
            # 1) 定义递归终止条件
            # 应该是从candidate选出来的数的sum(numbs)=target就返回，所以这时候递归层数i应该是候选值列表。
            # 修改递归参数第一个参数i为nums，表示一个候选值列表
            if sum(nums) == target:
                result.append(tuple(nums))
                return

            # 如果 sum(nums)>target 这时候也应该停止了，因为candidates都是正整数
            if sum(nums) > target:
                return

            # 2) 处理当前层逻辑
            # 当前层逻辑处理：如果sum(nums)<target，那么下一步nums中新增元素可能是candidates中的任一元素
            newNums = [nums + [i] for i in candidates]
            # 3）下探递归
            for nums in newNums:
                helper(nums)
            # 4）清理当前层，当前层没有要清理的

        # 3. 首次调用递归函数
        helper([])

        return [list(nums) for nums in result]

    def combinationSumV2(self, candidates, target):
        """递归代码优化，语言层面优化代码"""
        result = set()

        def helper(nums: List[int]):
            if sum(nums) == target:
                result.add(tuple(sorted(nums)))
                return

            if sum(nums) > target:
                return

            for i in candidates:
                helper(nums + [i])

        helper([])

        return [list(nums) for nums in result]
