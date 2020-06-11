# -*- coding:utf-8; -*-


class Solution:
    """
    递归解法思路：https://leetcode.com/problems/n-queens/discuss/19810/Fast-short-and-easy-to-understand-python-solution-11-lines-76ms
    """

    def solveNQueens(self, n):
        result = []

        def dfs(cols, xy_sum, xy_dif):
            row_idx = len(cols)
            if row_idx == n:
                result.append(cols)
                return

            for col_idx in range(n):
                if (
                    col_idx not in cols
                    and col_idx + row_idx not in xy_sum
                    and col_idx - row_idx not in xy_dif
                ):
                    dfs(
                        cols + [col_idx],
                        xy_sum + [col_idx + row_idx],
                        xy_dif + [col_idx - row_idx],
                    )

        dfs([], [], [])
        return [
            ["." * col + "Q" + "." * (n - col - 1) for col in plan] for plan in result
        ]
