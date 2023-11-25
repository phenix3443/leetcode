from typing import List


class Solution:
    """字母异位词分组"""

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for e in strs:
            k = tuple(sorted(e))
            d[k] = d.get(k, []) + [e]

        return list(d.values())
