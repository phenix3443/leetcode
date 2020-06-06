class Solution:
    """ 递归解法
    与46题目类似，可将重复元素换成数组下标
    """

    def permuteUnique(self, nums):
        result = []

        numsLen = len(nums)
        origNums = set([i for i in range(len(nums))])

        def helper(i, nums, r):
            if i == numsLen:
                result.append(r)
                return

            for k in origNums - set(r):
                helper(i + 1, nums, r + [k])

        helper(0, nums, [])
        return list(set([tuple([nums[i] for i in idxs]) for idxs in result]))
