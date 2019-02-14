class Solution:
    def reverse(self, x: 'int') -> 'int':
        org = x;
        if x < 0:
            x *= -1
        numStr = str(x)
        s = list(str)


s = Solution()
print(s.reverse(123))
