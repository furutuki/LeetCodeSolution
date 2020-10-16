class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        low = 0
        high = len(A) - 1
        ans = []
        while low <= high:
            m = A[low] * A[low]
            n = A[high] * A[high]
            if n >= m:
                ans.append(n)
                high -= 1
            else:
                ans.append(m)
                low += 1
        return ans[::-1]