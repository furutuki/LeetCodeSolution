from collections import defaultdict
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = defaultdict(int)
        s = [False for _ in range(2001)]
        for item in arr:
            d[item] += 1
        for item in d.values():
            if item > 0:
                if s[item + 1000]:
                    return False
                else:
                    s[item + 1000] = True
        return True
