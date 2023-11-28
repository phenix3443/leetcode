import unittest


class Solution:
    """爬楼梯"""

    def climbStairs(self, n):
        """递归算法，但是提示超时"""
        if n < 3:
            return n
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    def climbStairsV1(self, n: int) -> int:
        if n < 3:
            return n

        dp = [1] * n
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[-1]

    def climbStairsV2(self, n: int) -> int:
        if n < 3:
            return n

        f1, f2 = 1, 2
        for i in range(3, n + 1):  # 注意这里为什么是n+1
            f3 = f1 + f2
            f1, f2 = f2, f3

        return f3


class TestClimbStairs(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Solution().climbStairs(2), 2)
        self.assertEqual(Solution().climbStairs(3), 3)

    def test_2(self):
        self.assertEqual(Solution().climbStairsV1(2), 2)
        self.assertEqual(Solution().climbStairsV1(3), 3)


if __name__ == "__main__":
    unittest.main()
