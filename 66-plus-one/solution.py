# -*- coding:utf-8; -*-


class Solution:
    """
    找到最后一个不是9的位置，那么
    1. 该位置以后的数字直接置零
    2. 如果该位置存在，只需将该位置+1即可
    3. 该位置如果不存在，那么说明整个数组都是9，那么头部需要增加一位，该位必定是1

    如果是将数组换成单链表，使用双指针，该思路同样可行。
    """

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
