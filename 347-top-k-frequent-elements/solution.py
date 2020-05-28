# -*- coding:utf-8; -*-
import heapq


class Solution:
    def topKFrequent(self, nums, k):
        m = {}
        for e in nums:
            m[e] = m[e] + 1 if e in m else 1

        ret = heapq.nlargest(k, [(v, k) for k, v in m.items()])

        return [e[1] for e in ret]


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    s = Solution()
    print(s.topKFrequent(nums, k))
