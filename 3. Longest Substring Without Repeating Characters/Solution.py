class Solution:
    def lengthOfLongestSubstring(self, s: 'str') -> 'int':
        max_count = 0
        my_set = set()
        for startIndex in range(0, len(s)):
            for index in range(startIndex, len(s)):
                if s[index] in my_set:
                    if len(my_set) > max_count:
                        max_count = len(my_set)
                    del my_set
                    my_set = set()
                    break
                else:
                    my_set.add(s[index])

        if len(my_set) > 0 and len(my_set) > max_count:
            max_count = len(my_set)

        return max_count


s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("pwwkew"))
print(s.lengthOfLongestSubstring(" "))
