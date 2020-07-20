class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        p = 0
        q = 1
        for i in range(2, n + 1):
            v = p + q
            p = q
            q = v
        return v
