from typing import List

import heapq


class Solution:
    """数组中的第 K 个最大元素"""

    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        建立一个大根堆，做 k−1k - 1k−1 次删除操作后堆顶元素就是我们要找的答案。
        了解对排序算法
        """
        if len(nums) < k:
            return 0

        ret = heapq.nlargest(k, nums)

        return ret[-1]
