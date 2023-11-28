from typing import List
import unittest


class Solution:
    """四数之和"""

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        return self.nSum(nums, target, 4)

    def nSum(self, nums, target, n):
        def dfs(pos, cur, n, target):
            if n == 2:
                j = pos
                k = len(nums) - 1
                while j < k:
                    sum = nums[j] + nums[k]
                    if sum < target:
                        j += 1
                    elif sum > target:
                        k -= 1
                    else:
                        solution = cur[:] + [nums[j], nums[k]]
                        ans.append(solution)
                        while j < k and nums[j] == nums[j + 1]:
                            j += 1
                        while j < k and nums[k] == nums[k - 1]:
                            k -= 1
                        j += 1
                        k -= 1
                return
            i = pos
            while i < len(nums) - n + 1:
                # 剪枝的一种情况
                if nums[i] * n > target or nums[-1] * n < target:
                    break
                # 排除重复数字
                if i > pos and nums[i] == nums[i - 1]:
                    i += 1
                    continue
                cur.append(nums[i])
                dfs(i + 1, cur, n - 1, target - nums[i])  # 递归处理
                cur.pop()
                i += 1

        ans = []  # 存储结果
        nums.sort()
        dfs(0, [], n, target)
        return ans


class TestFourSum(unittest.TestCase):
    def test_four_sum(self):
        self.assertEqual(
            Solution().fourSum([1, 0, -1, 0, -2, 2], 0),
            [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]],
        )


if __name__ == "__main__":
    unittest.main()
