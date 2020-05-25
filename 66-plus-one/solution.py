# -*- coding:utf-8; -*-
class Solution:
    def plusOne(self, digits):
        lastNot9 = -1
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] ^ 9:
                lastNot9 = i
                break
            else:
                digits[i] &= 0

        if lastNot9 == -1:
            digits.insert(0, 1)  # 这个时候最高位肯定应该是1
        else:
            digits[lastNot9] += 1

        return digits


if __name__ == "__main__":
    digits = [9, 9]
    s = Solution()
    print(s.plusOne(digits))
