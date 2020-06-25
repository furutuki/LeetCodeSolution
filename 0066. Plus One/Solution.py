from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = 0
        digits[len(digits) - 1] = digits[len(digits) - 1] + 1
        for idx in range(len(digits) - 1, -1, -1):
            s = (int)((digits[idx] + a) / 10)
            digits[idx] = (digits[idx] + a) % 10
            a = s
        if a == 0:
            return digits
        else:
            res = [];
            res.append(1)
            res.extend(digits)
            return res


s = Solution()
print(s.plusOne([1,2,3]))
print(s.plusOne([4,3,2,1]))
print(s.plusOne([0]))
