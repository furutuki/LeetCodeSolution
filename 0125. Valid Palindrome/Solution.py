import re


class Solution:

    def isPalindrome(self, s: str) -> bool:

        s = re.sub('[^a-zA-Z0-9]', '', s)

        if len(s) == 0:
            return True

        for i in range(0, (int)(len(s) / 2) + 1):
            if s[i].lower() != s[len(s) - 1 - i].lower():
                return False

        return True


s = Solution()
print(s.isPalindrome(""))
print(s.isPalindrome("0P"))
print(s.isPalindrome("A man, a plan, a canal: Panama"))
print(s.isPalindrome("race a ca"))
