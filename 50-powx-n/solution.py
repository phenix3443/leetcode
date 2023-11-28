import unittest


class Solution:
    """快速幂"""

    def fastPow(self, x: float, n: int):
        if n == 0:
            return 1

        half = self.fastPow(x, n >> 1)  # n/2 使用位运算避免小数

        return half * half * (1 if n & 1 == 0 else x)  # n&1 达到n%2

    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        return self.fastPow(x, n)


class TestMyPow(unittest.TestCase):
    def test_myPow(self):
        self.assertEqual(Solution().myPow(2.00000, 10), 1024.0)
        self.assertEqual(Solution().myPow(2.00000, -2), 0.25000)


if __name__ == "__main__":
    unittest.main()
