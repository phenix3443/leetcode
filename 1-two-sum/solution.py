class Solution:
    def twoSum(self, nums, target):
        m = {}  # 存储将要查找的数
        for i, v in enumerate(nums):
            x = m.get(v)
            if x is None:
                m[target - v] = i
            else:
                return [x, i]
