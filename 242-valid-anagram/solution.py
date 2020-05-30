# -*- coding:utf-8; -*-


class SolutionSort:
    """排序
    """

    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)


class SolutionMap:
    """使用map
    """

    def isAnagram(self, s, t):
        m = {}
        for i in s:
            m[i] = m[i] + 1 if i in m else 1
        for i in t:
            m[i] = m[i] - 1 if i in m else -1

        for (k, v) in m.items():
            if v != 0:
                return False

        return True
