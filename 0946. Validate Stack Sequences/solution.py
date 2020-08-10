from typing import List


class Solution:

    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        s = []
        dic = {}
        idx = 0
        for i in range(len(popped)):
            if dic.__contains__(popped[i]):
                if s[len(s) - 1] == popped[i]:
                    del s[len(s) - 1]
                else:
                    return False
            else:
                while idx < len(pushed) and pushed[idx] != popped[i]:
                    s.append(pushed[idx])
                    dic[pushed[idx]] = True
                    idx += 1
                idx += 1
        return not s