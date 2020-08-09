from typing import List


class Solution:
    def printNumbers(self, n: int) -> List[int]:
        border = pow(10, n)
        res = list()
        for i in range(1, border):
            res.append(i)
        return res