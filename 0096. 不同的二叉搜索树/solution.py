class Solution:
    def numTrees(self, n: int) -> int:
        "dp[i]  i个节点能构建的方案数"
        dp = [0 for _ in range(n + 1)]
        dp[0], dp[1] = 1, 1
        for i in range(2, n + 1):
            for j in range(i):
                "j来枚举左子树节点数，去掉根，右节点数就是i - j - 1"
                dp[i] += dp[j] * dp[i - j - 1]
        return dp[n]
