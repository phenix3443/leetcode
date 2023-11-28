from typing import List
import unittest


class SolutionV1:
    """电话号码的字母组合"""

    def letterCombinations(self, digits: str) -> List[str]:
        # 1. 定义一个集合存储最后的字符串
        result = []

        # 2. 然后定义一个递归函数，来生成符合条件的字符串
        # 递归函数的参数如何定义：
        # i 表示递归层数，这里的含义已经处理到电话号码的第i位了
        def helper(s):
            # 3. 首先写递归模板
            # 1）递归终止条件
            # 5. 阅读题意，终止条件应该是：字符串的长度=len(digits)
            if len(s) == len(digits):
                # 4. 如果满足，就应该将字符串返回
                result.append(s)
                return
            # 2) 处理当前层
            # 6. 当前层处理逻辑是什么呢？应该是s+ (digit[i]上对应的字母)，但是每个数字对应多个字母，所以有当前会有多种结果，这时候需要定义一个map，用于遍历数字对应的字母
            digitAlpha = {
                "2": ["a", "b", "c"],
                "3": ["d", "e", "f"],
                "4": ["g", "h", "i"],
                "5": ["j", "k", "l"],
                "6": ["m", "n", "o"],
                "7": ["p", "q", "r", "s"],
                "8": ["t", "u", "v"],
                "9": ["w", "x", "y", "z"],
            }
            newS = []
            for c in digitAlpha[digits[len(s)]]:
                newS.append(s + c)
            # 3）递归处理下一层：对所有新生成的s调用递归函数，生成新长度的s

            for s in newS:
                helper(s)
            # 4）清理当前层：当前层没有需要清理的

        helper("")
        return result


class Solution:
    """从语言层面优化一下v1代码"""

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digitAlpha = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        result = []
        digits_len = len(digits)

        def helper(s):
            i = len(s)
            if i == digits_len:
                result.append(s)
                return

            for c in digitAlpha[digits[i]]:
                helper(s + c)

        helper("")
        return result


class TestLetterCombinations(unittest.TestCase):
    def test_letterCombinations(self):
        s = Solution()
        self.assertEqual(
            s.letterCombinations("23"),
            ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"],
        )


if __name__ == "__main__":
    unittest.main()
