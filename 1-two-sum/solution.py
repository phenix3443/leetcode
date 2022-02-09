# -*- coding:utf-8; -*-


class Solution:
    def twoSum(self, nums, target):
        m = {}  # 存储将要查找的数
        for i, v in enumerate(nums):
            x = m.get(v)
            if x == None:
                m[target - v] = i
            else:
                return [x, i]


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))
