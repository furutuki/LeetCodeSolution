import collections


class Solution:
    def firstUniqChar(self, s: str) -> str:
        d = collections.OrderedDict()
        for c in s:
            d[c] = not c in d
        for k, v in d.items():
            if v:
                return k
        return ' '