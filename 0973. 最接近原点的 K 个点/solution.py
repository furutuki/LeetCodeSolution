from typing import List
import math


class Node:
    def __init__(self, item: List[int]):
        self.data = item
        self.sqrt = math.sqrt(item[0] * item[0] + item[1] * item[1])

    def __eq__(self, other):
        return self.sqrt == other.sqrt

    def __lt__(self, other):
        return self.sqrt < other.sqrt


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        tmp = []
        for point in points:
            tmp.append(Node(point))
        tmp.sort()
        ans = []
        for i in range(K):
            ans.append(tmp[i].data)
        return ans


s = Solution()
print(s.kClosest([[1, 3], [-2, 2]], 1))
