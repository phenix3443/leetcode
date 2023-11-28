from typing import List
import unittest


class Solution:
    """三角形最小路径和"""

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """动态规划思路：
        1. 动态规划定义：dp[i][j]表示triangle[i][j]节点的最短路径。
        2. 动态规划方程：dp[i][j] = min{dp[i+1][j],dp[i+1][j+1]}+triangle[i][j]
        3. 边界条件：最后一维数组。
        """
        dp = triangle.copy()
        for i in range(len(dp) - 2, -1, -1):
            row = triangle[i]
            for j, v in enumerate(row):
                dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1]) + v

        return dp[0][0]


class TestMinimumTotal(unittest.TestCase):
    def test_1(self):
        triangle = [
            [2],
            [3, 4],
            [6, 5, 7],
            [4, 1, 8, 3],
        ]
        target = Solution().minimumTotal(triangle)
        self.assertEqual(target, 11)


if __name__ == "__main__":
    unittest.main()
