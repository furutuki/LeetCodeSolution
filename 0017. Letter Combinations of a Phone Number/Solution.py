from typing import List

class Solution:

    def lists_combination(self, lists, code=''):
        try:
            import reduce
        except:
            from functools import reduce

        def myfunc(list1, list2):
            s =  [str(i) + code + str(j) for i in list1 for j in list2]
            return s

        if len(lists) == 0:
            return []
        else:
            return reduce(myfunc, lists)


    def letterCombinations(self, digits: str) -> List[str]:
        s = [[], [], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'],
             ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]

        input_list = []
        for i in range(len(digits)):
            input_list.append(s[int(digits[i])])

        return self.lists_combination(input_list)


s = Solution()
print(s.letterCombinations(""))
