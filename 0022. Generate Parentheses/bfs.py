from typing import List
import collections


class Result(object):

    def __init__(self, s: str, wrap: bool, d: int):
        self.items = s
        self.wrapped = wrap
        self.depth = d


class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        q = collections.deque()
        if n == 0:
            return []
        else:
            q.appendleft(Result("()", False, 1))

        self.bfs(q, n)

        result = list()
        while len(q) > 0:
            item = q.pop()
            result.append(item.items)

        return result

    def bfs(self, q: collections.deque, n: int):
        while len(q) > 0:
            if q[-1].depth >= n:
                break

            item = q.pop()
            if item.wrapped:
                new_item_0 = Result("(" + item.items + ")", True, item.depth + 1)
                new_item_1 = Result(item.items + "()", True, item.depth + 1)
                new_item_2 = Result("()" + item.items, True, item.depth + 1)
                q.appendleft(new_item_0)
                q.appendleft(new_item_1)
                q.appendleft(new_item_2)
            else:
                new_item_1 = Result("(" + item.items + ")", True, item.depth + 1)
                new_item_2 = Result("()" + item.items, False, item.depth + 1)
                q.appendleft(new_item_1)
                q.appendleft(new_item_2)


s = Solution()
print(s.generateParenthesis(4))
