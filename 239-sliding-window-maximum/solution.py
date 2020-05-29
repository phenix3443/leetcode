# -*- coding:utf-8; -*-
"""
解题思路：
1. 暴力求解，每次都求k个数中的最大值，时间复杂度O(k),该操作需要执行n-k次，总体复杂度O(n^2)
2. 转换思路：
   1. 要求位置i左边最大的数？典型的单调栈问题。
   2. 单调递减栈的性质：当位置i位于栈顶时(stack[-1]=i)，从栈顶到栈底，栈中元素对应的取值都>=a[i],小于a[i]的位置都已经被弹出。因为求得是最大值，所以弹出的这些元素都<a[i],也不用考虑。
   3. 最大数的位置有范围限制 [i-k+,i]，由于是单调栈，那么只需要判断栈底是不是stack[0]<i-k+1即可，如果是就弹出栈底，如果不是，这时候栈底对应的取值stack[0]就是所求值.
   4. 其实这道题是单调栈的延伸，是单调队列，每个数组元素都进出队列一次，所以时间复杂度是O(n)
"""


class Solution:
    def maxSlidingWindow(self, nums, k):
        l = len(nums)
        res = []
        stack = []
        for i in range(l):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            stack.append(i)

            if i >= k - 1:  # 因为是从第K的元素开始计算的框中的最大值的
                while stack and stack[0] < i - k + 1:  # i-k+1是框中第一个元素
                    stack = stack[1:]
                res.append(nums[stack[0]])

        return res


if __name__ == "__main__":
    # nums = [1, 3, -1, -3, 5, 3, 6, 7]
    # k = 3
    nums = [1, -1]
    k = 1
    s = Solution()
    print(s.maxSlidingWindow(nums, k))
