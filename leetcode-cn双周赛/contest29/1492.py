class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        # mid = n // 2
        res = set()
        for i in range(1, n + 1):
            if n % i == 0:
                res.add(i)
                res.add((n // i))

        if len(res) < k:
            return -1

        l = list(res)
        l.sort()
        return l[k - 1]


s = Solution()
print(s.kthFactor(1,1))
