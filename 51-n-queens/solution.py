from typing import List
import unittest


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """N皇后"""

        res = []

        def helper(cols: List[int], xy_sum: List[int], xy_dif: List[int]):
            """
            DFS+剪枝：https://zhuanlan.zhihu.com/p/81849845
            1. cols[i] 表示 i 行的皇后所在列号
            2. xy_sum[i], xy_dif[i]表示 i 行的皇后所在对角线冲突条件
            """
            r = len(cols)  # 当前行号
            if r == n:
                res.append(cols)
                return

            for c in range(n):  # 当前行每一列放置皇后的可行性
                if c not in cols and c + r not in xy_sum and c - r not in xy_dif:
                    helper(
                        cols + [c],
                        xy_sum + [c + r],
                        xy_dif + [c - r],
                    )

        helper([], [], [])
        return [["." * col + "Q" + "." * (n - col - 1) for col in plan] for plan in res]


class TestNQueens(unittest.TestCase):
    def test_solveNQueens(self):
        self.assertEqual(
            Solution().solveNQueens(4),
            [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]],
        )


if __name__ == "__main__":
    unittest.main()
