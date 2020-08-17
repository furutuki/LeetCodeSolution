from typing import List


class Solution:
    def perm(self, s: str, idx: int, ans: set):
        n = len(s)
        if idx == n:
            return list(ans)

        tmp = set()
        for item in list(ans):
            for i in range(len(item) + 1):
                l = list(item)
                l.insert(i, s[idx])
                tmp.add("".join(l))
        return self.perm(s, idx + 1, tmp)


    def permutation(self, s: str) -> List[str]:
        return self.perm(s, 1, {s[0]}) if s else []