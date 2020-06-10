# -*- coding:utf-8; -*-


class Solution:
    """ 思路：就是用2，3，5不断分解原来的数字

    """

    def isUgly(self, num):
        for i in [2, 3, 5]:
            while num > 1:  # 注意判断条件
                if num % i == 0:  # 是否能够被2,3,5整除
                    num /= i  # 下次递归
                else:  # 一直算到i的质因数完
                    break

        return num == 1


if __name__ == "__main__":
    n = 10
    s = Solution()
    print(s.isUgly(n))
