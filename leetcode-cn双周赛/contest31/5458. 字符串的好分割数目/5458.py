from typing import List


class Solution:
    def numSplits(self, s: str) -> int:
        m = len(s)
        if m == 1:
            return 0

        count = 0

        left = dict()
        right = dict()
        left[s[0]] = 1

        for i in range(m - 1, 0, -1):
            if right.__contains__(s[i]):
                right[s[i]] += 1
            else:
                right[s[i]] = 1

        if len(right.keys()) == 1:
            count += 1

        for i in range(1, m - 1):
            if not left.__contains__(s[i]):
                left[s[i]] = 1
            else:
                left[s[i]] += 1

            if right[s[i]] > 1:
                right[s[i]] -= 1
            else:
                del right[s[i]]

            if len(left) == len(right):
                count += 1

        return count

s = Solution()
print(s.numSplits("abcd"))
print(s.numSplits("aaaaa"))
print(s.numSplits("acbadbaada"))
print(s.numSplits("aacaba"))