import math
import unittest


class Solution:
    """排列序列"""

    def getPermutation(self, n: int, k: int) -> str:
        nums = [0] * n

        numsList = [i for i in range(1, n + 1)]
        print(numsList)
        for i in range(0, n):
            fnums = math.factorial(
                n - i - 1
            )  # 表示位置i后面数字所有的组合，比如第一位后面的排列组合有(n-1)!
            idx = (
                math.ceil(k / fnums) - 1
            )  # 计算当前i应该是取的序号，减一是因为numList排序从1开始
            nums[i] = numsList.pop(idx)
            k = k % fnums

        return "".join(map(str, nums))


class TestGetPermutation(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Solution().getPermutation(3, 3), "213")

    def test_2(self):
        self.assertEqual(Solution().getPermutation(4, 9), "2314")


if __name__ == "__main__":
    unittest.main()
