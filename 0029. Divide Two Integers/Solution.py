class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        res = 0
        if dividend != 0:
            aa = abs(dividend)
            bb = abs(divisor)
            while aa > bb:
                count = 1
                base = bb
                while aa > base:
                    base <<= 1
                    if aa > base:
                        count <<= 1
                aa -= (base >> 1)
                res += count

            if aa == bb:
                res += 1

        if dividend / divisor < 0:
            res *= -1
        if res > 2**31 - 1:
            return 2 ** 31 - 1
        return res


s = Solution()
print(s.divide(-2147483648, -1))

