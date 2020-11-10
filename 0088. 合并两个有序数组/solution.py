from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        length = m
        while i < length and j < n:
            if nums1[i] >= nums2[j]:
                start = j
                while j < n and nums1[i] >= nums2[j]:
                    j += 1
                cnt = j - start
                nums1[i + cnt:] = nums1[i:]
                nums1[i:i+cnt] = nums2[start:j]
                length += cnt
                i += cnt
            else:
                i += 1
        while j < n:
            nums1[i] = nums2[j]
            i += 1
            j += 1
        del nums1[m+n:]

