from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        if not s:
            return None

        res = ['' for _ in range(len(s))]

        for i in range(len(s)):
            res[indices[i]] = s[i]

        return ''.join(res)



s = Solution()
print(s.restoreString("codeleet", [4,5,6,7,0,2,1,3]))
