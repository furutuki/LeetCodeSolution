class Solution:
    def isPalindrome(self, x: 'int') -> 'bool':
        num = list(str(x))
        for x in range(0, len(num)):
            if num[x] != num[len(num) - x - 1]:
                return False
        return True


s = Solution()
print(s.isPalindrome(121))
print(s.isPalindrome(-121))
