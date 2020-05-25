# -*- coding:utf-8; -*-
class Solution:
    def plusOne(self, digits):
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1
            if digits[i] ^ 10:  # 异或判断是否不相等
                return digits
            else:
                digits[i] &= 0

        digits.insert(0, 1)  # 这个时候最高位肯定应该是1
        return digits


if __name__ == "__main__":
    digits = [9]
    s = Solution()
    print(s.plusOne(digits))
