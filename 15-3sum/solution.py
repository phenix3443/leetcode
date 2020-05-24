# -*- coding:utf-8; -*-
class Solution:
    def twoSum(self, nums, target):
        # nums是有序的
        if nums[0] > target:
            return

        m = {nums[0]: 0}
        r = []  # result
        i = 1
        numsLen = len(nums)
        while i < numsLen:
            other = target - nums[i]
            if other in m:
                r.append([other, nums[i]])
                while i < numsLen - 1 and nums[i + 1] == nums[i]:  # skip same
                    i += 1

            m[nums[i]] = i

            i += 1

        return r

    def threeSum(self, nums):
        ret = []

        nums.sort()  # 排序后方便two-sum夹逼

        for k in range(len(nums) - 2):
            if nums[k] > 0:  # 最小的数字已经大于0了，放弃
                break
            if k > 0 and nums[k] == nums[k - 1]:  # skip same
                continue

            ts = self.twoSum(nums[k + 1 :], 0 - nums[k])

            if ts:
                ret.extend([(nums[k], t[0], t[1]) for t in ts])

            k += 1

        return ret


if __name__ == "__main__":
    s = Solution()
    print(s.threeSum([-2, 0, 1, 1, 2]))
