from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        "f[i] means subarray(0, i) can represented by word of wordDict"
        f = [False for i in range(len(s) + 1)]

        f[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if f[j] and wordDict.__contains__(s[j:i]):
                    f[i] = True
                    break
        return f[len(s)]


s = Solution()
print(s.wordBreak(("leetcode"), ["leet", "code"]))

