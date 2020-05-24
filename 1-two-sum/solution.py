# -*- coding:utf-8; -*-
class Solution:
    def twoSum(self, nums, target):
        m = {}  # use the empty dict to avoid the compare location with self

        for i in range(len(nums)):
            another_idx = m.get(target - nums[i])
            if not (another_idx is None):
                return [another_idx, i]  # because second_num_idx<i

            m[nums[i]] = i

        return


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))
