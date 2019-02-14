class Solution:
    def reverse(self, x: 'int') -> 'int':
        negative_flag = False
        if x < 0:
            x *= -1
            negative_flag = True
        num_str = str(x)
        s = list(num_str)
        s.reverse()
        reversed_int = int(''.join(s))
        if negative_flag:
            result = -1 * reversed_int
        else:
            result = reversed_int

        if -1 * 2**31 <= result < 2 ** 31:
            return result
        else:
            return 0


s = Solution()
print(s.reverse(123))
print(s.reverse(-123))
print(s.reverse(120))
print(s.reverse(-120))
print(s.reverse(123456789999))
