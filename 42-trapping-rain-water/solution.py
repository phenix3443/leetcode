# -*- coding:utf-8; -*-
"""
解题思路：
观察每个水洼：
1. 水洼的高度，取决于最低点两侧最后一根单调递增的柱子（）的高度（记做H），单调边界问题，可能要使用单调栈。
2. 水洼的宽度=
一个柱子顶部水的面积，取决于柱子两侧第一个高度超过该柱本身的柱子的最短值。
这样，整个问题就转化为递减单调栈的问题了。注意，没有左侧或者右侧没有比当前更高的柱子，那么该柱子顶部没有水。

"""


class Solution:
    def trap(self, heights):
        area = 0
        stack = []
        for i in range(len(heights)):
            while stack and heights[stack[-1]] < heights[i]:
                idx = stack.pop()
                h = heights[idx]  # 当前柱子的高度
                if not stack:
                    break

                l = stack[-1]  # 左侧第一个比当前柱子高的柱子
                r = i  # 右侧第一个比当前柱子高的柱子
                w = (min(heights[l], heights[r]) - h) * (r - l - 1)
                print(idx, h, w)
                area += w

            stack.append(i)

        print(stack)
        return area


if __name__ == "__main__":
    heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    s = Solution()
    print(s.trap(heights))
