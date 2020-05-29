# -*- coding:utf-8; -*-
"""
思路：f(n)表示n的丑数序号
f(n) = f(n-1)+ (1 if n%2%3%5==0 else 0)
f(0)=0
f(1) =1
"""


class Solution:
    def helper(self, n):
        for k in [2, 3, 5]:
            while n > 0:
                if n % k == 0:
                    n = n / k
                else:
                    break

        return n == 1

    def nthUglyNumber(self, k):
        if k in [0, 1]:
            return k

        n, fn = 1, 1
        while fn < k:
            pre = fn
            n += 1
            fn = pre + (1 if self.helper(n) else 0)

        return n


if __name__ == "__main__":
    n = 11
    s = Solution()
    print(s.nthUglyNumber(n))
