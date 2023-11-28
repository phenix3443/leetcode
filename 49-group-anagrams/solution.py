from typing import List
import unittest


class Solution:
    """字母异位词分组"""

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for e in strs:
            k = tuple(sorted(e))
            d[k] = d.get(k, []) + [e]

        return list(d.values())


class TestGroupAnagrams(unittest.TestCase):
    def test_groupAnagrams(self):
        self.assertEqual(
            Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]),
            [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]],
        )


if __name__ == "__main__":
    unittest.main()
