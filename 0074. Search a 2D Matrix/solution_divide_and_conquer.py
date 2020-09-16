from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        row, col = len(matrix), len(matrix[0])
        low, high = 0, row * col - 1
        while low <= high:
            mid = (low + high) // 2
            m = mid // col
            n = mid % col
            if matrix[m][n] == target:
                return True
            elif matrix[m][n] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False


s = Solution()
print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 3))
print(s.searchMatrix([[1,3]], 1))
print(s.searchMatrix([[1,3]], 8))