from typing import List
import unittest


class Solution:
    """括号生成"""

    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def helper(left, right, s):
            if left == n and right == n:
                result.append(s)
            if left < n:
                helper(left + 1, right, s + "(")
            if right < left:
                helper(left, right + 1, s + ")")

        helper(0, 0, "")
        return result


class TestGenerateParenthesis(unittest.TestCase):
    def test_generateParenthesis(self):
        self.assertEqual(
            Solution().generateParenthesis(3),
            ["((()))", "(()())", "(())()", "()(())", "()()()"],
        )


if __name__ == "__main__":
    unittest.main()
