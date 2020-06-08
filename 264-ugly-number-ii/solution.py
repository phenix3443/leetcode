# -*- coding:utf-8; -*-


import heapq


class SolutionV1:
    """ 回溯解法：
    使用最小堆排序，时间复杂度O(nlogn)，空间复杂度O(2n)
    """

    def nthUglyNumber(self, k):

        hp = [1]
        existNums = set([1])  # 用于最小堆去重

        heapq.heapify(hp)

        nth = 0
        for i in range(k):
            nth = heapq.heappop(hp)  # 取出第i个丑数
            for j in [2, 3, 5]:  # 为什么要执行这一步呢？是因为我们知道，后续的丑数都是当前这个最小的丑数*[2,3,5]得出的。
                newNum = nth * j
                if newNum not in existNums:
                    existNums.add(newNum)
                    heapq.heappush(hp, newNum)

        return nth


class Solution:
    """递归解法：
    dp和递归的区别就是dp记录了第n个解前面的状态，进而我们先尝试使用一维数组dp[n]，记录第n个丑数。
    根据上面V1的求解过程，我们可以得知，第i次的最小值是取集合中的最小值。集合是dp[0]...dp[n-1]分别乘以2,3,5，然后减去dp[0]到dp[n-1]。
    最终 dp[n]=min{dp[0:n-1]*[2,3,5]-dp[0:n-1]}
    dp[0:n-1]*[2,3,5] 这个集合可以表示为下面的形式：
    乘以2的结果集：dp[0]*2 , dp[1]*2 ... dp[n-1]*2
    乘以3的结果集：dp[0]*3 , dp[1]*3 ... dp[n-1]*3
    乘以5的结果集：dp[0]*5 , dp[1]*5 ... dp[n-1]*5
    因为dp[0]到dp[n-1] 是递增的，所以其实我们只需要比较三个结果集中尚未使用（因为有的值已经是dp[i]）的第一个最小的那个数值即可，所以我们需要需要记录三个坐标i2,i3,i5，代表
    三个集合中最小值dp[i]对应的位置。

    找到对应的i2,i3,i5后，因为对应数值已经在计算最小值的时候用了，所以应该递增1，比如选中dp[i]=dp[i2]*2，那么下一步i2+=1,
    又因为i2,i3,i5之间可能有交集，比如dp[6]=dp[3]*2 ,dp[6]=dp[2]*3,所以i2,i3,i5都已经做检查。

    所以dpz状态方程：dp[n]=min{dp[i2]*2，dp[i3]*3,dp[i5]*5}
    初始条件dp[0]=1, i2=i3=i5=0
    """

    def nthUglyNumber(self, k):
        dp = [-1] * k
        dp[0] = 1
        i2, i3, i5 = 0, 0, 0

        for i in range(1, k):
            dp[i] = min(dp[i2] * 2, dp[i3] * 3, dp[i5] * 5)
            if dp[i2] * 2 == dp[i]:
                i2 += 1
            if dp[i3] * 3 == dp[i]:
                i3 += 1
            if dp[i5] * 5 == dp[i]:
                i5 += 1

        return dp[k - 1]


if __name__ == "__main__":
    k = 1
    s = Solution()
    print(s.nthUglyNumber(k))
