# -*- coding:utf-8; -*-
class Solution:
    def twoSum(self, nums, target):
        m = {}  # 使用空的集合，避免之前本身相加的判断

        for i in range(len(nums)):
            l = m.get(target - nums[i])
            if not (l is None):
                return [l, i]  # 因为必定l<i

            m[nums[i]] = i

        return


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))
