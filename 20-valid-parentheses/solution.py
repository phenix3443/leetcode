# -*- coding:utf-8; -*-
class Solution:
    def isValid(self, s):
        m = {")": "(", "]": "[", "}": "{"}
        stack = []
        for c in s:
            if c not in m:  # 不是右括号
                if c == " ":
                    continue
                else:
                    stack.append(c)
                    continue
            else:
                # 遇到右括号
                if not stack:  # 栈空
                    return False
                else:
                    if stack[len(stack) - 1] != m[c]:  # 顶端元素不匹配
                        return False
                    else:
                        stack.pop()

        return True if not stack else False


if __name__ == "__main__":
    s = Solution()
    print(s.isValid("()"))
