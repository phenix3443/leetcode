# -*- coding:utf-8; -*-


class Solution:
    def isAnagram(self, s, t):
        m = {}
        for i in s:
            m[i] = m[i] + 1 if i in m else 1
        for i in t:
            m[i] = m[i] - 1 if i in m else -1

        for (k, v) in m.items():
            if v != 0:
                return False
        else:
            return True
