# -*- coding:utf-8; -*-

"""
思路：将手写的方法转化为代码，关键在于如何理清楚递归的四个步骤

"""


class SolutionV1:
    def generateParenthesis(self, n):
        # 因为最终结果是一个列表，所以先定义一个保存结果的地方
        result = []
        # 应该有一个递归函数，递归函数的作用就是生成一个个的合法的字符串
        # 逐步填充这个结构，定义递归函数，i表示递归层级，虽然i的具体含义还可能不知道
        def helper(i, n, s):
            # 开始编写低估函数的四个步骤:
            # 1. 终止条件
            # 递归终止的时候应该将正确的字符串放入result，那么字符串s就必然应该是递归函数的一个参数。
            # 那什么是递归条件呢？很明显：是字符串长度中左右括号的数量等于n时。此时，参数i的具体含义也就清楚了：i表示当前字符串中左右括号的个数。
            if i == n:
                result.append(s)
                return
            # 2. 处理当前层逻辑
            # 此时i<n，表示字符串s左右扩好还没有满，可以继续追加，但是此时有既可以追加左括号，也可以追加右括号
            s1 = s + "("
            s2 = s + ")"
            # 到这里的时候，当前层级已经没有更多的处理，那么接下来应该怎么继续递归？
            # 下一层要做的事情和当前层要做的事情相同：就是决定是给上层传过来的字符s添加左括号还是右括号
            # 但是第二步发现，当前层可能生成两个后续处理的字符串，s1和s2，所以这里应该有两个递归。
            # 3. 递归往下
            helper(i + 1, n, s1)
            helper(i + 1, n, s2)

            # 4. 清理当前层
            # 最后过一下，当前层没有要处理的代码。

        # 为什么只有一次递归函数调用，就可以在result中生成多个结果呢？
        # 为什么这里不是for循环？每次循环向result增加一个结果？
        # 是因为最终结构其实就是这个递归书的叶子节点，每个叶子节点的逻辑中都执行了一次 result.append
        helper(0, n, "")
        return result


class SolutionV2:
    """ 技术上优化V1的代码，同时进一步分析代码
    """

    def generateParenthesis(self, n):
        result = []

        def helper(i, n, s):
            if i == n:
                # 此时只是将左右括号的全排列找了出来，但并不一定是符合题目要求的有效排列，所以此处要加一个校验
                def valid(s):
                    return True

                if valid(s):
                    result.append(s)
                    return

            helper(i + 1, n, s + "(")
            helper(i + 1, n, s + ")")

        helper(0, n, "")
        return result


class Solution:
    """ v2 中的valid函数其实在当前层添加左右括号的时候，就可以判断，这个的确不好想，记下来就好。
    """

    def generateParenthesis(self, n):
        result = []

        def helper(left, right, n, s):
            if left == n and right == n:
                result.append(s)
            if left < n:
                helper(left + 1, right, n, s + "(")
            if right < left:
                helper(left, right + 1, n, s + ")")

        helper(0, 0, n, "")
        return result
