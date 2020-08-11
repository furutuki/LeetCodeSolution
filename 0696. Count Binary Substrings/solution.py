class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans = 0
        last, cur = 0, 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cur += 1
            else:
                last = cur
                cur = 1
            if last >= cur:
                ans += 1
        return ans

