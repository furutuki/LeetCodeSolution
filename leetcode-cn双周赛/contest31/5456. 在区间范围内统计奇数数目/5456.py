class Solution:
    def countOdds(self, low: int, high: int) -> int:
        a = low % 2 == 0
        b = high % 2 == 0
        cnt = (high - low -  1) // 2
        if (high - low - 1) % 2 != 0:
            if a:
               cnt += 1
            else:
                cnt += 2
        else:
            cnt += 1
        return cnt

s = Solution()
print(s.countOdds(21,22))
print(s.countOdds(3,7))
print(s.countOdds(4,8))
print(s.countOdds(4,9))
print(s.countOdds(3, 8))

