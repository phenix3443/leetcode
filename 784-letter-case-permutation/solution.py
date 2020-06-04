# -*- coding:utf-8; -*-


class Solution:
    def letterCasePermutation(self, S):
        res = set()

        def helper(i, n, s):
            if i == n:
                res.add(s)
                return

            helper(i + 1, n, s[:i] + s[i].lower() + s[i + 1 :])
            helper(i + 1, n, s[:i] + s[i].upper() + s[i + 1 :])

        helper(0, len(S), S)

        return [s for s in res]


if __name__ == "__main__":
    S = "C"
    s = Solution()
    print(s.letterCasePermutation(S))
