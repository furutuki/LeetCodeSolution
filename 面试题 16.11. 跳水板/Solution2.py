from typing import List


class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if k == 0:
            return []

        if shorter == longer:
            return [shorter * k]

        res = []
        smallest = shorter * k
        diff = longer - shorter
        for i in range(k, -1, -1):
            res.append(smallest + diff * (k - i))

        return res


s = Solution()
print(s.divingBoard(2, 1118596, 979))
