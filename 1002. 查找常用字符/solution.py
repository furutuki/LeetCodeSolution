from collections import OrderedDict
from typing import List


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if not A:
            return []

        cnt = len(A)
        d = [OrderedDict()for _ in range(cnt)]

        "建立字典数组"
        for i in range(cnt):
            for ch in A[i]:
                if ch in d[i]:
                    d[i][ch] += 1
                else:
                    d[i][ch] = 1

        for key in d[0]:
            val = d[0][key]
            for i in range(1, cnt):
                if key in d[i]:
                    val = min(val, d[i][key])
                else:
                    val = 0
                    break
            d[0][key] = val
        ans = []
        for key in d[0]:
            for times in range(d[0][key]):
                ans.append(key)
        return ans


s = Solution()
print(s.commonChars(["bella","label","roller"]))