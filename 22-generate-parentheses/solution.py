from typing import List


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
