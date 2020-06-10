# -*- coding:utf-8; -*-
class Solution:
    def isValid(self, s):
        m = {")": "(", "]": "[", "}": "{"}
        stack = []
        for c in s:
            if c not in m:  # 不是右括号
                if c != " ":
                    stack.append(c)
                continue
            else:
                # 遇到右括号
                if not (stack and stack[-1] == m[c]):  # 栈空
                    return False
                else:
                    stack.pop()

        return False if stack else True


if __name__ == "__main__":
    s = Solution()
    print(s.isValid("()"))
