from typing import List


class Solution:
    def __init__(self):
        self.ans = []

    def dfs(self,  s: str, index: int, count: int, res: str):
        if count > 4:
            return

        if count == 4:
            if index == len(s):
                self.ans.append(res)
            return

        for step in range(1, 4, 1):
            if index + step <= len(s) and int(s[index:index + step]) <= 255 and (step == 1 or s[index] != '0'):
                tmp = res
                if count > 0:
                    res += "."
                res += s[index:index + step]
                self.dfs(s, index + step, count + 1, res)
                res = tmp

    def restoreIpAddresses(self, s: str) -> List[str]:
        self.ans = []
        self.dfs(s, 0, 0, "")
        return self.ans


s = Solution()
print(s.restoreIpAddresses("25525511135"))