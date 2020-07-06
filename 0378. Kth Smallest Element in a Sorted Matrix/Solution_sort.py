from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l = list()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                l.append(matrix[i][j])
        l.sort()
        return l[k - 1]