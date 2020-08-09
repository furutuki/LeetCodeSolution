class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = list()
        m, n = len(num1), len(num2)
        i, j = m - 1, n - 1
        p = 0
        while i >= 0 and j >= 0:
            tmp = p + int(num1[i]) + int(num2[j])
            p = tmp // 10
            res.append(str(tmp % 10))
            i -= 1
            j -= 1

        while i >= 0:
            tmp = p + int(num1[i])
            p = tmp // 10
            res.append(str(tmp % 10))
            i -= 1
        while j >= 0:
            tmp = p + int(num2[j])
            p = tmp // 10
            res.append(str(tmp % 10))
            j -= 1
        if p > 0:
            res.append(str(p))

        res.reverse()
        return "".join(res)

s = Solution()
print(s.addStrings("6", "501"))
