# -*- coding:utf-8;x -*-
class Solution:
    def groupAnagrams(self, strs):
        d = {}
        for e in strs:
            k = tuple(sorted(e))
            d[k] = d.get(k, []) + [e]

        return list(d.values())


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    s = Solution()
    print(s.groupAnagrams(strs))
