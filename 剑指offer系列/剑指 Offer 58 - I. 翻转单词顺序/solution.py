class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])


s = Solution()
ss = s.reverseWords("  hello world!  ")
print(ss)
