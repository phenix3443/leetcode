# -*- coding:utf-8; -*-
"""
"""


class Solution:
    def isUgly(self, num):
        while num > 1:
            for i in [2, 3, 5]:
                if num % i == 0:  # 是否能够被2,3,5整除
                    num /= i  # 下次递归
                    break
            else:
                break

        return num == 1


if __name__ == "__main__":
    n = 0
    s = Solution()
    print(s.isUgly(n))
