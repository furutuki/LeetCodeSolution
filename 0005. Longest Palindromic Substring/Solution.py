class Solution:
    def longestPalindrome(self, s: 'str') -> 'str':
        matrix = [[False for x in range(len(s))] for y in range(len(s))]
        for i in range(0, len(s)):
            matrix[i][i] = True
        max_length = 0
        start_index = 0
        end_index = 0
        for j in range(1, len(s)):
            for i in range(0, j):
                if s[i] == s[j] and (i + 1 == j or matrix[i + 1][j - 1]):
                    matrix[i][j] = True
                    if j - i + 1 > max_length:
                        start_index = i
                        end_index = j
                        max_length = j - i + 1
        return s[start_index:end_index + 1]
        # max_count = 0
        # result_str = ""
        #
        # for i in range(0, len(s)):
        #     for j in range(i + max_count, len(s)):
        #         substring = s[i:j+1]
        #         reversed_str = substring[::-1]
        #         if substring == reversed_str and len(substring) > max_count:
        #             max_count = len(substring)
        #             result_str = substring
        # return result_str


s = Solution()
print(s.longestPalindrome("bb"))
print(s.longestPalindrome("ac"))
print(s.longestPalindrome("a"))
print(s.longestPalindrome("babad"))
print(s.longestPalindrome("cbbd"))
