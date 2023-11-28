from typing import List
import unittest


class Solution:
    """组合"""

    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 0:
            return []

        result = []

        def helper(combination: List[int]):
            if len(combination) == k:
                result.append(combination)
                return

            start = combination[-1] + 1 if combination else 1  # 这里是重点
            for m in range(start, n + 1):
                helper(combination + [m])

        helper([])

        return result


class TestCombine(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            Solution().combine(4, 2), [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
        )

    def test_2(self):
        self.assertEqual(Solution().combine(1, 1), [[1]])


if __name__ == "__main__":
    unittest.main()
