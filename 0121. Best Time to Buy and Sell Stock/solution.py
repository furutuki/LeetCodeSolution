from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """ index of minimum item of prices[0...i]"""
        min_index = 0

        """ max profit in section prices[0...i]"""
        cur_max = 0
        for i in range(1, len(prices)):
            cur_max = max(cur_max, prices[i] - prices[min_index])
            min_index = min_index if prices[min_index] <= prices[i] else i
        return cur_max


s = Solution()
print(s.maxProfit([1,2,11,4,7]))
print(s.maxProfit([2,1,2,1,0,1,2]))
print(s.maxProfit([2,1,4]))
print(s.maxProfit([7,1,5,3,6,4]))
print(s.maxProfit([7,6,4,3,1]))