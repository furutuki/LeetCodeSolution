from typing import List


class Solution:

    def dfs(self, ret: List[str], parenthesis: str, left_cnt: int, right_cnt: int, n: int):
        if len(parenthesis) == 2 * n:
            ret.append(parenthesis)
        else:
            if left_cnt < n:
                self.dfs(ret, parenthesis + "(", left_cnt + 1, right_cnt, n)
            if right_cnt < left_cnt:
                self.dfs(ret, parenthesis + ")", left_cnt, right_cnt + 1, n)

    def generateParenthesis(self, n: int) -> List[str]:
        ret = list()
        self.dfs(ret, "", 0, 0, n)
        return ret


s = Solution()
print(s.generateParenthesis(3))
