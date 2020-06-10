# -*- coding:utf-8; -*-
import sys


class Solution:
    """
    动态规划思路：
    1. 状态定义：dp[i]表示 数值i对应的最少钱币数量。
    2. 转移方程：dp[i] = min{dp[i-coins[j]]}+1  0<=j<len(coins)
    3. 边界条件： dp[0] =0
    """

    def coinChange(self, coins, amount):
        dp = [0] * (amount + 1)
        for i in range(1, amount + 1):
            pre = [dp[i - j] for j in coins if i - j >= 0]
            dp[i] = min(pre) + 1 if pre else sys.maxsize

        return dp[amount] if dp[amount] < sys.maxsize else -1


if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11
    # coins = [2]
    # amount = 3
    s = Solution()
    print(s.coinChange(coins, amount))
