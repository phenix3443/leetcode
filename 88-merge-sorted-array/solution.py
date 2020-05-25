# -*- coding:utf-8; -*-


class Solution:
    def merge(self, nums1, m, nums2, n):
        i, j, p = m - 1, n - 1, m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[p] = nums1[i]
                i -= 1
            elif nums1[i] < nums2[j]:
                nums1[p] = nums2[j]
                j -= 1

            p -= 1

        if j >= 0:
            nums1[p - j : p + 1] = nums2[0 : j + 1]


if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    s = Solution()
    s.merge(nums1, m, nums2, n)
    print(nums1)
