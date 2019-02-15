class Solution:
    def myAtoi(self, str: 'str') -> 'int':
        res_str = ''
        i = 0
        while i < len(str):
            while i < len(str) and str[i] == ' ':
                i += 1
            if i == len(str):
                return 0

            if str[i].isdigit() or ((str[i] == '-' or str[i] == '+') and (i + 1 < len(str) and str[i + 1].isdigit())):
                if not str[i].isdigit():
                    res_str += str[i]
                    i += 1
                while i < len(str) and str[i].isdigit():
                    res_str += str[i]
                    i += 1
                break
            else:
                return 0
        if len(str) == 0:
            return 0
        num = int(res_str)
        if num > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif num < -1 * 2 ** 31:
            return -1 * 2 ** 31
        else:
            return num


s = Solution()
print(s.myAtoi('42'))
print(s.myAtoi('-42'))
print(s.myAtoi('4193 with words'))
print(s.myAtoi('word and 987'))
print(s.myAtoi('-91283472332'))
