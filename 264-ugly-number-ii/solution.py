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
    def nthUglyNumber(self, k):
        pass


if __name__ == "__main__":
    k = 10
    s = Solution()
    print(s.nthUglyNumber(k))
