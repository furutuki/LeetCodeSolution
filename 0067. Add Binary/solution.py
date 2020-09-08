class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m, n = len(a) - 1, len(b) - 1
        res = ""
        p = 0
        while m >= 0 or n >= 0:
            aa = 0 if m < 0 else a[m]
            bb = 0 if n < 0 else b[n]
            tmp = int(aa) + int(bb) + p
            res += str(tmp % 2)
            p = tmp // 2
            m -= 1
            n -= 1
        if p > 0:
            res += str(p)
        return res[::-1]

s = Solution()
print(s.addBinary("1010", "1011"))