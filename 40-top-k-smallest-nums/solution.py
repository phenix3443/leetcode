# - *-coding: utf - 8; - *-

import heapq


class Solution:
    def getLeastNumbers(self, arr, k):
        if k == 0:
            return []

        if len(arr) <= k:
            return arr

        return heapq.nsmallest(k, arr)


if __name__ == "__main__":
    arr = [0, 0, 1, 2, 4, 2, 2, 3, 1, 4]
    k = 8
    s = Solution()
    print(s.getLeastNumbers(arr, k))
