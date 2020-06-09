# -*- coding:utf-8; -*-


class Solution:
    """动态规划思路：
    1. DP状态定义：dp[i][j]，其中0<=i<len(nums),j=[0,1]
       dp[i][0] 表示包含nums[i] 时候最小乘积,dp[i][1] 表示包含nums[i] 时候最大乘积。
    2. DP状态转移方程：
       if nums[i] < 0:
           dp[i][0] = dp[i-1][1] * nums[i]
           dp[i][1] = dp[i-1][0] * nums[i]
        else:
           dp[i][0] = dp[i-1][0] * nums[i]
           dp[i][1] = dp[i-1][1] * nums[i]

        进一步简化：

        dp[i][0] = min(dp[i - 1][0] * nums[i], dp[i - 1][1] * nums[i], nums[i])
        dp[i][1] = max(dp[i - 1][0] * nums[i], dp[i - 1][1] * nums[i], nums[i])

        不要忘记nums[i]，因为序列也能包含一个元素

    3. DP边界
       dp[0][0] = dp[0][1] = nums[0]
    """

    def maxProduct(self, nums):
        if not nums:
            return 0
        dp = [[0 for i in range(2)] for j in range(len(nums))]

        res = dp[0][0] = dp[0][1] = nums[0]

        for i in range(1, len(nums)):
            dp[i][0] = min((dp[i - 1][0]) * nums[i], (dp[i - 1][1]) * nums[i], nums[i])
            dp[i][1] = max(dp[i - 1][0] * nums[i], dp[i - 1][1] * nums[i], nums[i])
            res = max(res, dp[i][1])

        return res


if __name__ == "__main__":
    nums = [2, 3, -2, 4]
    s = Solution()
    print(s.maxProduct(nums))
