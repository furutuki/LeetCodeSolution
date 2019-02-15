class Solution:
    def romanToInt(self, s: 'str') -> 'int':
        mapping = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
                   'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        i = 0
        total = 0
        while i < len(s):
            if (s[i] == 'I' or s[i] == 'X' or s[i] == 'C') and (i + 1 < len(s) and mapping.get(s[i:i + 2]) is not None):
                total += mapping.get(s[i:i+2])
                i += 2
            else:
                total += mapping.get(s[i:i+1])
                i += 1
        return total


s = Solution()
print(s.romanToInt("III"))
print(s.romanToInt("IV"))
print(s.romanToInt("LVIII"))
