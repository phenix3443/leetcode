# -*- coding:utf-8; -*-
class Solution:
    def threeSum(self, nums):
        ret = set()

        nums.sort()  # 排序后方便two-sum夹逼

        for i, v in enumerate(nums[:-2]):
            if v > 0:  # 最小的数字已经大于0了，放弃
                break

            if i > 0 and nums[i] == nums[i - 1]:  # skip same
                continue

            d = {}
            for x in nums[i + 1 :]:
                if x not in d:  # 这里处理比较巧妙，要好好想想，因为d肯定是在nums了，下一步只要找到-v-x就可以了
                    d[-v - x] = 1
                else:
                    ret.add((v, x, -v - x))

        return [list(e) for e in ret]


if __name__ == "__main__":
    s = Solution()
    print(s.threeSum([0, 0, 0, 0]))
