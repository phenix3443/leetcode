# -*- coding:utf-8; -*-
import math


class Solution:
    def getPermutation(self, n, k):
        nums = [0] * n

        numsList = [i for i in range(1, n + 1)]
        print(numsList)
        for i in range(0, n):
            fnums = math.factorial(n - i - 1)  # 表示位置i后面数字所有的组合，比如第一位后面的排列组合有(n-1)!
            idx = math.ceil(k / fnums) - 1  # 计算当前i应该是取的序号，减一是因为numList排序从1开始
            nums[i] = numsList.pop(idx)
            k = k % fnums

        return "".join(map(str, nums))


if __name__ == "__main__":
    n = 4
    k = 9
    s = Solution()
    print(s.getPermutation(n, k))  # 213
