from typing import List


class Result(object):

    def __init__(self, s: str, wrap: bool):
        self.items = s
        self.wrapped = wrap


class Solution:
    ret = []

    def generateParenthesis(self, n: int) -> List[str]:
        self.gen(self.ret, 1, n)
        temp = self.ret[n - 1]
        result = list()
        for item in temp:
            result.append(item.items)
        return result

    def gen(self, ret: List, cur: int, n: int):
        if (cur == 1):
            ret.insert(0, [Result("()", False)])

        else:
            lastResList = ret[cur - 2]
            ret.insert(cur - 1, [])

            for item in lastResList:
                if item.wrapped:
                    new_item_0 = Result("(" + item.items + ")", True)
                    new_item_1 = Result("()" + item.items, True)
                    new_item_2 = Result(item.items + "()", True)
                    ret[cur - 1] = ret[cur - 1] + [new_item_0, new_item_1, new_item_2]
                else:
                    new_item_1 = Result("(" + item.items + ")", True)
                    new_item_2 = Result("()" + item.items, False)
                    ret[cur - 1] = ret[cur - 1] + [new_item_1, new_item_2]

        if cur < n:
            self.gen(ret, cur + 1, n)


s = Solution()
print(s.generateParenthesis(4))
