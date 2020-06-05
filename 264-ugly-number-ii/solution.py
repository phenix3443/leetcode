# -*- coding:utf-8; -*-


import heapq


class SolutionV1:
    """ 使用最小堆排序，时间复杂度O(nlogn)，空间复杂度O(2n)
    """

    def nthUglyNumber(self, k):

        hp = [1]
        existNums = set([1])  # 用于最小堆去重

        heapq.heapify(hp)

        nth = 0
        for i in range(k):
            nth = heapq.heappop(hp)  # 取出第i个丑数
            for j in [2, 3, 5]:
                newNum = nth * j
                if newNum not in existNums:
                    existNums.add(newNum)
                    heapq.heappush(hp, newNum)

        return nth


class Solution:
    """
    DP状态定义：DP[i]表示第i个丑数
    DP状态方程：DP[i] = min(DP[],DP[i-1],DP[i-1])
    """

    def nthUglyNumber(self, k):
        nums = [1]  # 按序保存丑数
        idx = {2: 0, 3: 0, 5: 0}  # 2,3,5对应的最小的丑数在nums中的位置
        for i in range(k):
            nth = min(nums[idx[2]], nums[idx[3]], nums[idx[5]])

        return nth or 0


if __name__ == "__main__":
    k = 1
    s = Solution()
    print(s.nthUglyNumber(k))
