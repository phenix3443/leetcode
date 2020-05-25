# -*- coding:utf-8; -*-


class Solution:
    def reverse(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    def rotate(self, nums, k):
        l = len(nums)
        k %= l
        self.reverse(nums, 0, l - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, l - 1)


if __name__ == "__main__":
    nums = [-1, -100, 3, 99]
    k = 3
    s = Solution()
    s.rotate(nums, k)
    print(nums)
