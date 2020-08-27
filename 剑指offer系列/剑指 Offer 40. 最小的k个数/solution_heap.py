from typing import List
import heapq

class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        ans = []
        heapq.heapify(arr)
        while k > 0:
            ans.append(heapq.heappop(arr))
            k -= 1
        return ans
