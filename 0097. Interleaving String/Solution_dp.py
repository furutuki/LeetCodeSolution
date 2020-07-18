class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)
        p = len(s3)

        if m + n != p:
            return False

        f = [[False for i in range(n + 1)] for _ in range(m + 1)]

        f[0][0] = True

        for i in range(m + 1):
            for j in range(n + 1):
                if i > 0 and s1[i - 1] == s3[i + j - 1] and f[i - 1][j]:
                    f[i][j] = True
                elif j > 0 and s2[j - 1] == s3[i + j - 1] and f[i][j - 1]:
                    f[i][j] = True

        return f[m][n]


s = Solution()
print(s.isInterleave("aabcc", "dbbca", "aadbbcbcac"))
