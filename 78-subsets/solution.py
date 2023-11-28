from typing import List
import unittest


class Solution:
    """子集"""

    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        递归思路：假设初始为空的subset，途经nums中每个元素时候，可以选中也可以不选中。
        """
        res = []

        def helper(i, sub: List[int]):
            # 1. 递归终止条件
            if i == len(nums):
                res.append(sub)
                return
            # 2. 处理当前逻辑
            # 3. 下探递归
            helper(i + 1, sub)
            helper(i + 1, sub + [nums[i]])
            # 清理当前层

        helper(0, [])

        return res

    def subsetsV2(self, nums: List[int]) -> List[List[int]]:
        """
        动态规划思路：假设f(n) 表示n个元素的所求集合，那么 f(n) = f(n-1) + nums[n]*f(n-1)
        nums[n]*f(n-1) 表示nums[n] 与 f(n-1) 中每个集合做的并集后形成的集合。比如f(n-1) 为 [[1],[1,2]], nums[n]=3,
        nums[n]*f(n-1) = [[1,3],[1,2,3]]
        """
        res = [[]]

        def helper(i):
            if i == len(nums):
                return

            res.extend([sub + [nums[i]] for sub in res])

            helper(i + 1)

        helper(0)
        return res


class TestSubsets(unittest.TestCase):
    def test_subsets(self):
        solution = Solution()
        assert sorted(solution.subsets([1, 2, 3])) == sorted(
            [[3], [1], [2], [1, 2, 3], [1, 3], [2, 3], [1, 2], []]
        )
        assert sorted(solution.subsetsV2([1, 2, 3])) == sorted(
            [[3], [1], [2], [1, 2, 3], [1, 3], [2, 3], [1, 2], []]
        )


if __name__ == "__main__":
    unittest.main()
