class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        m, n = 0, len(s) - 1
        i, j = 0, len(t) - 1

        while i <= j and m <= n:
            if t[i] == s[m]:
                m += 1
                i += 1
            else:
                i += 1

            if t[j] == s[n]:
                j -= 1
                n -= 1
            else:
                j -= 1
        return m > n


s = Solution()
print(s.isSubsequence("aa", "ahbgdc"))