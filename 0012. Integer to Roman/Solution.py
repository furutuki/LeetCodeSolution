class Solution:
    def intToRoman(self, num: 'int') -> 'str':
        my_list = [[1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'], [100, 'C'], [90, 'XC'],
                   [50, 'L'], [40, 'XL'], [10, 'X'], [9, 'IX'], [5, 'V'], [4, 'IV'], [1, 'I']]
        res = ''
        while num > 0:
            for i in range(0, len(my_list)):
                if num >= my_list[i][0]:
                    for j in range(0, num // my_list[i][0]):
                        res += my_list[i][1]
                    num = num % my_list[i][0]
        return res


s = Solution()
print(s.intToRoman(3))
print(s.intToRoman(4))
