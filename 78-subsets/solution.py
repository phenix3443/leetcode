# -*- coding:utf-8; -*-


class SolutionV1:
    """ 思路：假设初始为空的subset，途经nums中每个元素时候，可以选中也可以不选中。
    """

    def subsets(self, nums):
        res = []

        def helper(i, nums, sub):
            if i == len(nums):
                res.append(sub)
                return

            helper(i + 1, nums, sub)
            helper(i + 1, nums, sub + [nums[i]])

        helper(0, nums, [])

        return res


class SolutionV2:
    """ 思路：假设f(n) 表示n个元素的所求集合，那么 f(n) = f(n-1) + nums[n]*f(n-1)
        nums[n]*f(n-1) 表示nums[n] 与 f(n-1) 中每个集合做的并集后形成的集合。比如f(n-1) 为 [[1],[1,2]], nums[n]=3,
        nums[n]*f(n-1) = [[1,3],[1,2,3]]
    """

    def subsets(self, nums):
        res = [[]]

        def helper(i, nums):
            if i == len(nums):
                return

            res.extend([sub + [nums[i]] for sub in res])

            helper(i + 1, nums)

        helper(0, nums)
        return res


if __name__ == "__main__":
    nums = [1, 2, 3]
    s = SolutionV2()
    print(s.subsets(nums))
