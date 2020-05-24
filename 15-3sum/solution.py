# -*- coding:utf-8; -*-
class Solution:
    def threeSum(self, nums):
        ret = set()

        nums.sort()  # 排序后方便two-sum夹逼

        for k in range(len(nums) - 2):
            if nums[k] > 0:  # 最小的数字已经大于0了，放弃
                break
            if k > 0 and nums[k] == nums[k - 1]:  # skip same
                continue

            l, r = k + 1, len(nums) - 1
            while l < r:
                s = nums[k] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:  # skip same
                        l += 1
                elif s > 0:
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:  # skip same
                        r -= 1
                else:
                    ret.add((nums[k], nums[l], nums[r]))
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
            k += 1

        return list(ret)


if __name__ == "__main__":
    s = Solution()
    print(s.threeSum([-2, 0, 1, 1, 2]))
