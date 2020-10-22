from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        rightMostPos = dict()
        for i in range(len(S) - 1, -1, -1):
            if S[i] not in rightMostPos:
                rightMostPos[S[i]] = i

        left, right = 0, 0
        ans = []
        while True:
            right = rightMostPos[S[left]]
            cursor = left + 1
            while cursor <= right:
                if rightMostPos[S[cursor]] > right:
                    right = rightMostPos[S[cursor]]
                cursor += 1
            ans.append(right - left + 1)
            left = right + 1
            if left >= len(S):
                break
        return ans

