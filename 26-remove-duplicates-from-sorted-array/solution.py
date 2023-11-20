from typing import List


class Solution:
    """删除排序数组中的重复项"""

    def removeDuplicates(self, nums: List[int]) -> int:
        lastUniq, i = 0, 0  # 前面唯一序列的最后一个元素
        for v in nums[1:]:
            v = nums[i]
            if v != nums[lastUniq]:
                lastUniq += 1
                nums[lastUniq] = v

        return lastUniq + 1
