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
            hp.put(0 - e)

        top = 0 - hp.get()  # 表示第K大个元素，这里这么绕是因为head(hp)没有heap.top() 方法
        for e in arr[k:]:  # 这个时候堆肯定是满的
            if e < top:
                hp.put(0 - e)
                top = 0 - hp.get()

        hp.put(0 - top)

        ret = [0 - hp.get() for i in range(k)]
        ret.reverse()

        return ret


if __name__ == "__main__":
    arr = [0, 0, 1, 2, 4, 2, 2, 3, 1, 4]
    k = 8
    s = Solution()
    print(s.getLeastNumbers(arr, k))
