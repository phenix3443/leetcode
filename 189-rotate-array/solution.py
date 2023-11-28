from typing import List


class Solution:
    """轮转数组"""

    def rotate(self, nums: List[int], k: int) -> None:
        """
        如果不考虑空间复杂度，这个问题其实是一个循环队列的问题:
        1. 关键是考虑到位置i元素后续移动k次后，所在的位置 newIdx=(i+k)%n,
        2. 若果这个问题变成向左移动，newIdx=(i-k)%n。即使考虑循环队列计数。
        """
        s, tmp = len(nums), nums.copy
        for i, v in enumerate(tmp):
            newIdx = (i + k) % s
            nums[newIdx] = v

    def rotateV2(self, nums: List[int], k: int) -> None:
        """
        使用两次反转，不大好想，记下来就行了。
        """

        def reverse(self, nums: List[int], i: int, j: int) -> None:
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        l = len(nums)
        k %= l
        reverse(nums, 0, l - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, l - 1)


if __name__ == "__main__":
    nums = [-1, -100, 3, 99]
    k = 3
    s = Solution()
    s.rotate(nums, k)
    print(nums)
