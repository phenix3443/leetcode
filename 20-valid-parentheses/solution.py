import unittest


class Solution:
    """有效的括号"""

    def isValid(self, s: str) -> bool:
        m = {")": "(", "]": "[", "}": "{"}
        stack = []
        for c in s:
            if c not in m:  # 左括号直接入栈
                stack.append(c)
            elif not stack or m[c] != stack.pop():  # 右括号需要判断
                return False
        return not stack


class TestIsValid(unittest.TestCase):
    def test_isValid(self):
        self.assertEqual(Solution().isValid("()"), True)
        self.assertEqual(Solution().isValid("()[]{}"), True)
        self.assertEqual(Solution().isValid("(]"), False)
        self.assertEqual(Solution().isValid("([)]"), False)
        self.assertEqual(Solution().isValid("{[]}"), True)
        self.assertEqual(Solution().isValid("]"), False)


if __name__ == "__main__":
    unittest.main()
