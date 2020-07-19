class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = m = numBottles
        while m >= numExchange:
            newBottles = m // numExchange
            total += newBottles
            m = m % numExchange + newBottles
        return total

s = Solution()
print(s.numWaterBottles(15, 4))
print((s.numWaterBottles(5, 5)))
print(s.numWaterBottles(2, 3))
