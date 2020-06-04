# -*- coding:utf-8; -*-


class Solution:
    def fastPow(self, x, n):
        if n == 0:
            return 1

        half = self.fastPow(x, n >> 1)  # n/2 使用位运算避免小数

        return half * half * (1 if n & 1 == 0 else x)  # n&1 达到n%2

    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n

        return self.fastPow(x, n)


if __name__ == "__main__":
    s = Solution()
    print(s.myPow(2.0, 10))
