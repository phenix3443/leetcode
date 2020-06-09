# -*- coding:utf-8; -*-
class Solution:
    """ 动态规划思路
    1. DP状态定义：dp[i] 表示包含nums[i] 时候的最长子序列的长度。
    2. DP状态转义方程:
       if nums[i] > num[0:i-1]:
           dp[i] = max{dp[0:i-1]} + 1
        else:
           dp[i] = 1                      #就是自身

    3. DP 边界:如果数组逆序，那么dp[i]=1
       dp[0] = 1
    """

    def lengthOfLIS(self, nums):
        if not nums:
            return 0

        dp = [1 for _ in nums]
        res = 1
        for i in range(1, len(nums)):
            dp[i] = max([(dp[j] + 1) if nums[i] > nums[j] else 1 for j in range(0, i)])
            res = max(res, dp[i])
        return res


if __name__ == "__main__":
    nums = [4, 10, 4, 3, 8, 9]
    s = Solution()
    print(s.lengthOfLIS(nums))
