class Solution:
    def multiply(self, num1: 'str', num2: 'str') -> 'str':
        return str(eval(num1 + " * " + num2))


s = Solution()
print(s.multiply("1232323234234234234234", "452342342342346"))
