class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        minus = True if n < 0 else False
        n = abs(n)
        while n > 0:
            if n % 2 == 1:
                res *= x
            x *= x
            n //= 2
        return 1 / res if minus else res
        # if n == 0:
        #     return 1
        # res = self.myPow(x, n // 2)
        # if n % 2 == 0:
        #     return res * res
        # else:
        #     return res * res * x