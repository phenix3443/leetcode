from typing import List
import unittest


class Solution:
    """最大乘积数组"""

    def maxProduct(self, nums: List[int]) -> int:
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
        if not nums:
            return 0

        # 因为每次都是使用前一个进行计算，所以只需要一个二位数组即可
        dp = [[0 for i in range(2)] for j in range(2)]

        res = dp[0][0] = dp[0][1] = nums[0]

        for i in range(1, len(nums)):
            # 巧妙的转换，因为每次都是使用前一个进行计算，所以只需要一个二位数组即可
            x, y = (
                i % 2,
                (i - 1) % 2,
            )
            t1 = dp[y][0] * nums[i]
            t2 = dp[y][1] * nums[i]
            dp[x][0] = min(t1, t2, nums[i])
            dp[x][1] = max(t1, t2, nums[i])
            res = max(res, dp[x][1])

        return res


class TestMaxProduct(unittest.TestCase):
    def test_1(self):
        nums = [2, 3, -2, 4]
        target = Solution().maxProduct(nums)
        self.assertEqual(target, 6)


if __name__ == "__main__":
    unittest.main()
