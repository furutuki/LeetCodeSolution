class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        idx = len(s) -1
        while idx >= 0 and s[idx] == ' ':
            idx -= 1

        if idx < 0:
            return 0

        for i in range(idx, -1, -1):
            if s[i] != ' ':
                length += 1
            else:
                break
        return length


s = Solution()
print(s.lengthOfLastWord("a"))
