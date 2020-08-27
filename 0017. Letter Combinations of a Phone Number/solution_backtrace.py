from typing import List

class Solution:

    def backtrace(self, lists):
        if len(lists) == 0:
            return []
        elif len(lists) == 1:
            return lists[0]
        res = []
        remain = self.backtrace(lists[1:])
        for alpha in lists[0]:
            for item in remain:
                res.append(alpha + "" + item)
        return res

    def letterCombinations(self, digits: str) -> List[str]:
        s = [[], [], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'],
             ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]

        input_list = []
        for i in range(len(digits)):
            input_list.append(s[int(digits[i])])

        return self.backtrace(input_list)

s = Solution()
print(s.letterCombinations("23"))
