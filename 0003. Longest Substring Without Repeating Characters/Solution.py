class Solution:
    def lengthOfLongestSubstring(self, s: 'str') -> 'int':
        max_count = 0
        my_set = set()
        start_index = 0
        tail_index = 0
        while start_index < len(s) and tail_index < len(s):
            if s[tail_index] in my_set:
                if len(my_set) > max_count:
                    max_count = len(my_set)

                pos = s[start_index:].find(s[tail_index]) + start_index
                del my_set
                my_set = set(list(s[pos + 1:tail_index + 1]))
                start_index = pos + 1
            else:
                my_set.add(s[tail_index])

            tail_index += 1

        if len(my_set) > 0 and len(my_set) > max_count:
            max_count = len(my_set)

        return max_count


s = Solution()
print(s.lengthOfLongestSubstring("dvdf"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("pwwkew"))
print(s.lengthOfLongestSubstring(" "))
