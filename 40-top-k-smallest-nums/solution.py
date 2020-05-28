# - *-coding: utf - 8; - *-
import queue


class Solution:
    def getLeastNumbers(self, arr, k):
        if k == 0:
            return []

        if len(arr) <= k:
            return arr

        hp = queue.PriorityQueue(k)

        for e in arr[:k]:
            hp.put(-e)

        for e in arr[k:]:  # 这个时候堆肯定是满的
            if e < -hp.queue[0]:
                hp.get()
                hp.put(-e)

        ret = [-e for e in hp.queue]

        return ret


if __name__ == "__main__":
    arr = [0, 0, 1, 2, 4, 2, 2, 3, 1, 4]
    k = 8
    s = Solution()
    print(s.getLeastNumbers(arr, k))
