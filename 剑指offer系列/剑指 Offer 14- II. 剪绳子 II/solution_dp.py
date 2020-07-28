class Solution:
    def cuttingRope(self, n: int) -> int:
        """dp[i] 表示长度为i的绳子的组大可能成绩"""
        dp = [0 for _ in range(n + 1)]
        dp[1] = 1

        for i in range(2, n + 1):
            for j in range(i // 2 + 1):
                tmp= max(i - j, dp[i - j]) * max(j, dp[j])
                dp[i] = max(tmp, dp[i])
        return dp[n] % 1000000007
