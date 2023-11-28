from typing import List
import unittest


class Solution:
    """跳跃游戏"""

    def canJump(self, nums: List[int]) -> bool:
        max_i = 0  # 初始化当前能到达最远的位置
        for i, jump in enumerate(nums):  # i为当前位置，jump是当前位置的跳数
            if (
                max_i >= i and i + jump > max_i
            ):  # 如果当前位置能到达，并且当前位置+跳数>最远位置
                max_i = i + jump  # 更新最远能到达位置
        return max_i >= len(nums) - 1


class TestCanJump(unittest.TestCase):
    def test_can_jump(self):
        self.assertEqual(Solution().canJump([2, 3, 1, 1, 4]), True)
        self.assertEqual(Solution().canJump([3, 2, 1, 0, 4]), False)


if __name__ == "__main__":
    unittest.main()
