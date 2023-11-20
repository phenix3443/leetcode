from typing import List


class Solution:
    """
    下一个排列
    Do not return anything, modify nums in-place instead.
    """

    def nextPermutation(self, nums: List[int]) -> None:
        """
        思路：关键是理解高位设置以后，其后的数字应该排列为最小的数值这一点。
        1. 倒序寻找第一个破坏升序的数nums[pos]。为什么这样查找，因为最大的那个数字排序肯定是倒序的。时间复杂度O(n),例如 [2,4,3,1] 中 2 破坏了升序。
        2. 然后在遍历过的数里倒序寻找（位权重从低到高）第一个比nums[pos]大的数字nums[i]，时间复杂度O(n)，该数字是3。
        3. 交换nums[pos]和nums[i]，这里交换2和3，新序列是[3,4,2,1]
        4. 将pos后面的数字改为升序，这是因为高位重新设置后,其后的数字应该排列成最小的数值，新的序列应该是[3,1,2,4]。
        """
        pos = len(nums) - 1
        while pos > 0 and nums[pos - 1] >= nums[pos]:
            pos -= 1

        if pos > 0:
            i = len(nums) - 1
            while i > pos - 1 and nums[i] <= nums[pos - 1]:
                i -= 1

            nums[pos - 1], nums[i] = nums[i], nums[pos - 1]

        i = pos
        j = len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
