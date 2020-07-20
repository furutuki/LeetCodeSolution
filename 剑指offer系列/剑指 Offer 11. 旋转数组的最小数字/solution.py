from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        n = len(numbers)

        if n == 1:
            return numbers[0]

        prev = 0
        cur = 1
        while cur < n and numbers[prev] <= numbers[cur]:
            cur += 1
            prev += 1
        if cur < n:
            return numbers[cur]
        else:
            return numbers[0]

s = Solution()
print(s.minArray([3,4,5,1,2]))
print(s.minArray([2,2,2,0,1]))