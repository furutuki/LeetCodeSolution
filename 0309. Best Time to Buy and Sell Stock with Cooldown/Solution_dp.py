from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        if length == 0: return 0
        # dp[i] 第 i 天结束后的状态
        # dp[i][0]: 不持有股票且不在冷冻期, dp[i][1]: 持有一支股票, dp[i][2] 在冷冻期.
        dp = [[0] * 3 for _ in range(length)]
        dp[0][1] = -prices[0]
        for i in range(1, length):
            # 前一天卖了，今天结束后没有股票同时刚好结束冷冻期，或者前一天不持有股票也不在冷冻期，今天休息
            dp[i][0] = max(dp[i-1][0], dp[i-1][2])
            # 今天买了，或者昨天有股票今天休息
            dp[i][1] = max(dp[i-1][0] - prices[i], dp[i-1][1])
            # 今天卖了之后处于冷冻期
            dp[i][2] = dp[i-1][1] + prices[i]
        return max(dp[-1][0], dp[-1][2])
