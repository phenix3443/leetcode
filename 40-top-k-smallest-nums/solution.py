# - *-coding: utf - 8; - *-

import math


class BinaryHeap:
    """"""

    def __init__(self, k):
        self.d = 2  # 二叉
        self.heapCap = k
        self.heapSize = 0
        self.heap = [-1] * (self.heapCap + 1)  # 多一个保证不越界

    def parent(self, i):
        return math.floor((i - 1) / self.d)

    def kthChild(self, i, k):
        return self.d * i + k

    def maxChild(self, i):
        leftChild = self.kthChild(i, 1)
        rightChild = self.kthChild(i, 2)
        return leftChild if self.heap[leftChild] > self.heap[rightChild] else rightChild

    def heapifyUp(self, i):
        v = self.heap[i]
        while i > 0 and v > self.heap[self.parent(i)]:  # 注意对比这段代码的逻辑
            self.heap[i] = self.heap[self.parent(i)]
            i = self.parent(i)

        self.heap[i] = v  # 不要忘记

    def heapifyDown(self, i):
        v = self.heap[i]
        while self.kthChild(i, 1) < self.heapSize:  # 注意对比这段代码逻辑，为什么要插左子树？因为是一颗完全二叉树
            child = self.maxChild(i)
            if v >= self.heap[child]:
                break
            self.heap[i] = self.heap[child]
            i = child

        self.heap[i] = v  # 不要忘记

    def put(self, e):
        if self.isFull():
            print("heap full")
            return

        self.heap[self.heapSize] = e
        self.heapSize += 1
        self.heapifyUp(self.heapSize - 1)

    def get(self, i):
        if self.isEmpty():
            print("heap emptry")
            return

        v = self.heap[i]
        self.heap[i] = self.heap[self.heapSize - 1]
        self.heapSize -= 1
        self.heapifyDown(i)

        return v

    def peek(self):
        return self.heap[0]

    def size(self):
        return self.heapSize

    def isFull(self):
        return self.heapSize == self.heapCap

    def isEmpty(self):
        return self.heapSize == 0

    def dump(self):
        return self.heap[: self.heapSize]

    def build(self, array):
        for e in array:
            self.put(e)


class Solution:
    def getLeastNumbers(self, arr, k):
        if k == 0:
            return []

        if len(arr) <= k:
            return arr

        hp = BinaryHeap(k)

        hp.build(arr[:k])

        for e in arr[k:]:  # 这个时候堆肯定是满的
            if e < hp.peek():
                hp.get(0)
                hp.put(e)

        return sorted(hp.dump())


if __name__ == "__main__":
    arr = [0, 0, 1, 2, 4, 2, 2, 3, 1, 4]
    k = 8
    s = Solution()
    print(s.getLeastNumbers(arr, k))
