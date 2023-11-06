from typing import Set


class Solution:
    def solveNQueens(self, n):
        """
        DFS+剪枝：https://zhuanlan.zhihu.com/p/81849845
        """
        res = []

        # cols[i] 表示 i 行的皇后所在列号
        # xy_sum[i], xy_dif[i]表示 i 行的皇后所在对角线冲突条件
        def dfs(cols, xy_sum, xy_dif):
            r = len(cols)  # 当前行号
            if r == n:
                res.append(cols)
                return

            for c in range(n):  # 当前行每一列放置皇后的可行性
                if c not in cols and c + r not in xy_sum and c - r not in xy_dif:
                    dfs(
                        cols + [c],
                        xy_sum + [c + r],
                        xy_dif + [c - r],
                    )

        dfs([], [], [])
        return [["." * col + "Q" + "." * (n - col - 1) for col in plan] for plan in res]
