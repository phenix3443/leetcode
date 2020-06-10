# -*- coding:utf-8; -*-
"""
解题思路：
首先通过观察发现：不管最大矩形怎么画，它的高度肯定等于某个柱子的高度（不考虑有等高柱子）。这个结论可以用反证法证明。

那么，问题就转变为，只要找到每个柱子作为高度时候的最大矩形，然后取其中最大值就对了，显然，这一层的时间复杂度是O(n)。

那么，一个柱子作为高度的最大矩形具有什么特点呢？观察就可以得出：两侧的柱子都比他高！同样反证法可以证明：如果两侧柱子都比他矮，那么以它为高度画出的矩形与题意不合。

那么，矩形面积=高度*宽度，高度已经确定（当前柱子的高度H）。宽度如何确定？继续观察，很明显，两侧的边界就是 *两侧出现的第一个低于H的柱子* 。这一步同样可以反证法。

最终，这个问题就转化为，在数组a中，怎么找到第i位数字两侧小于a[i]的位置。典型的单调栈。

"""


class Solution:
    def largestRectangleArea(self, heights):
        maxArea, stack = 0, []
        for i, v in enumerate(heights):
            while stack and heights[stack[-1]] > v:  # 单调递增栈，计算栈顶元素的左右边界
                h = heights[stack.pop()]  # 矩形高度
                l = stack[-1] if stack else -1  # 栈顶下面的元素是栈顶元素的左边界
                r = i  # 当前入栈元素是栈顶元素的右边界
                area = h * (r - l - 1)  # 计算面积
                maxArea = max(maxArea, area)

            stack.append(i)

        # 数组中剩余的元素是单调递增的，这些元素右侧都没与比他们矮的元素了
        for i in range(len(stack)):
            h = heights[stack.pop()]
            l = stack[-1] if stack else -1
            r = len(heights)
            area = h * (r - l - 1)
            maxArea = max(maxArea, area)

        return maxArea


if __name__ == "__main__":
    heights = [2, 1, 5, 6, 2, 3]
    s = Solution()
    print(s.largestRectangleArea(heights))
