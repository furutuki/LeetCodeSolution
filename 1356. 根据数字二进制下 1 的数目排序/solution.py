from typing import List
from collections import defaultdict

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        d = defaultdict(list)
        for num in arr:
            cnt = list(str(bin(num))).count('1')
            d[cnt].append(num)
        ans = []
        for i in range(15):
            ans.extend(sorted(d[i]) if d[i] else [])
        return ans