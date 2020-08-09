class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ""
        m, n = len(num1), len(num2)
        i, j = m - 1, n - 1
        p = 0
        while i >= 0 or j >= 0:
            a = int(num1[i]) if i >= 0 else 0
            b = int(num2[j]) if j >= 0 else 0
            tmp = a + b + p
            res = str(tmp % 10) + res
            p = tmp // 10
            i, j = i - 1, j - 1
        return "1" + res if p > 0 else res

s = Solution()
print(s.addStrings("6", "501"))
