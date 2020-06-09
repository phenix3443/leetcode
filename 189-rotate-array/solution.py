# -*- coding:utf-8; -*-


class SolutionV1:
    """如果不考虑空间复杂度，这个问题其实是一个循环队列的问题
       关键是考虑到位置i元素后续移动k次后，所在的位置 newIdx=(i+k)%n,
       若果这个问题变成向左移动，newIdx=(i-k)%n。即使考虑循环队列计数。

    """

    def rotate(self, nums, k):
        l = len(nums)
        tmp = nums.copy()
        for i, v in enumerate(tmp):
            newIdx = (i + k) % l
            nums[newIdx] = v


class Solution:
    """思路：
    使用两次反转，不大好想，记下来就行了。
    """

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
