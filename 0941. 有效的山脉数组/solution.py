from typing import List


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if not A or len(A) < 3:
            return False
        m, n = 0, 0
        i = 1
        while i < len(A) and A[i] > A[i - 1]:
            i += 1
            m = 2 if m == 0 else m + 1
        while i < len(A) and A[i] < A[i - 1]:
            i += 1
            n = 2 if n == 0 else n + 1
        return m > 0 and n > 0 and m + n == len(A) + 1

print(Solution().validMountainArray([0,3,2,1]))