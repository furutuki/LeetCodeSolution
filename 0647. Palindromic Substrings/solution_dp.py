class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        # dp[i][j] 表示[i:j]是个回文串
        dp = [[False for i in range(n)] for _ in range(n)]
        ans = 0
        for j in range(n):
            for i in range(j + 1):
                if i == j:
                    dp[i][j] = True
                elif i + 1 == j and s[i] == s[j]:
                    dp[i][j] = True
                elif j - i > 1 and s[i] == s[j]:
                    dp[i][j] =  dp[i + 1][j - 1]
                if dp[i][j]:
                    ans += 1
        return ans