import heapq

from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.q = nums
        heapq.heapify(self.q)
        while len(self.q) > self.k:
            heapq.heappop(self.q)

    def add(self, val: int) -> int:
        heapq.heappush(self.q, val)
        while len(self.q) > self.k:
            heapq.heappop(self.q)
        return self.q[0]
