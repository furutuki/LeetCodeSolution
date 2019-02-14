class Solution:
    def longestPalindrome(self, s: 'str') -> 'str':
        max_count = 0
        result_str = ""

        for i in range(0, len(s)):
            for j in range(i + max_count, len(s)):
                substring = s[i:j+1]
                reversed_str = substring[::-1]
                if substring == reversed_str and len(substring) > max_count:
                    max_count = len(substring)
                    result_str = substring
        return result_str


s = Solution()
print(s.longestPalindrome("bb"))
print(s.longestPalindrome("ac"))
print(s.longestPalindrome("a"))
print(s.longestPalindrome("babad"))
print(s.longestPalindrome("cbbd"))
