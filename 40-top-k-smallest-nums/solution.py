# - *-coding: utf - 8; - *-
import queue


class Solution:
    def getLeastNumbers(self, arr, k):
        if k == 0:
            return []

        if len(arr) <= k:
            return arr

        q = queue.PriorityQueue(k)

        for e in arr:
            if not q.full():
                q.put(0 - e)  # 以为优先队列默认是小根堆，但是需要将最大的数字挤出去
            else:
                e = -e
                top = q.get()
                if e > top:
                    q.put(e)
                else:
                    q.put(top)

        ret = [0 - q.get() for i in range(q.qsize())]
        ret.reverse()
        return ret


if __name__ == "__main__":
    arr = [0, 0, 1, 2, 4, 2, 2, 3, 1, 4]
    k = 8
    s = Solution()
    print(s.getLeastNumbers(arr, k))
