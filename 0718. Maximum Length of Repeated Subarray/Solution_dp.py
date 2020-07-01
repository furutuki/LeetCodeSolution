from typing import List


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        dp = [[0 for i in range(len(B) + 1)] for j in range(len(A) + 1)]
        max_num = 0
        for i in range(1, len(A) + 1):
            for j in range(1, len(B) + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    max_num = max(max_num, dp[i][j])
        return max_num


s = Solution()
print(s.findLength([1,2,3,2,1], [3,2,1,4,7]))
