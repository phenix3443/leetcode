# -*- coding:utf-8; -*-
class Solution:
    def dailyTemperatures(self, T):
        res = [0 for i in range(len(T))]
        stack = []
        for i in range(len(T)):
            # 1. 判断应该用递减栈
            # 2. 因为判断的是距离，所以栈中应该存储的是元素的位置
            while stack and T[stack[-1]] < T[i]:
                # 说明T[i]是栈顶元素右侧的第一个比自身大的元素
                l = stack.pop()
                res[l] = i - l

            stack.append(i)

        return res


if __name__ == "__main__":
    T = [73, 74, 75, 71, 69, 72, 76, 73]
    s = Solution()
    print(s.dailyTemperatures(T))
