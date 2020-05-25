# -*- coding:utf-8; -*-
class Solution:
    def plusOne(self, digits):
        nums = [0] + digits.copy()
        flag = True  # 表示是否有进位，初始1可以看做是低位进位
        for i in range(len(nums) - 1, -1, -1):
            if not flag:  # 没有进位，中断
                break
            else:  # 有进位
                if nums[i] < 9:
                    nums[i] += 1  # 直接+1，不产生进位
                    flag = False
                else:
                    nums[i] = 0  # 9置0，产生进位
                    flag = True

        if nums[0] == 0:  # 判断最高位是否为0
            return nums[1:]
        else:
            return nums


if __name__ == "__main__":
    digits = [9, 9, 9, 9]
    s = Solution()
    print(s.plusOne(digits))
