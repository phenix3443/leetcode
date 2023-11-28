from typing import List
import unittest


class Solution:
    """跳跃游戏 II"""

    def jump(self, nums: List[int]) -> int:
        step = 0
        step_end = 0  # 当前 step_start 能到达的最大下标位置
        max_bound = 0  # [step_start,step_end) 能到达的最大下标位置，记为边界。
        # 在遍历数组时，我们不访问最后一个元素，这是因为在访问最后一个元素之前，
        # 我们的边界一定大于等于最后一个位置，否则就无法跳到最后一个位置了。
        # 如果访问最后一个元素，在边界正好为最后一个位置的情况下，
        # 我们会增加一次「不必要的跳跃次数」，因此我们不必访问最后一个元素。
        for i, v in enumerate(nums[:-1]):
            max_bound = max(max_bound, v + i)
            if i == step_end:  # 到达边界时，更新边界并将跳跃次数增加 1
                step += 1
                step_end = max_bound
        return step


class TestJump(unittest.TestCase):
    def test_jump(self):
        self.assertEqual(Solution().jump([2, 3, 1, 1, 4]), 2)
        self.assertEqual(Solution().jump([2, 3, 0, 1, 4]), 2)


if __name__ == "__main__":
    unittest.main()
