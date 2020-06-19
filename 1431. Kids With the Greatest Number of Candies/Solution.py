from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandy = 0;
        for candy in candies:
            maxCandy = max(maxCandy, candy)

        res = []
        for candy in candies:
            res.append(extraCandies >= maxCandy - candy)
        return res


s = Solution()
print(s.kidsWithCandies([12, 1, 12], 10))
