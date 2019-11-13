from typing import List
from queue import Queue

class Solution:

    def canJump(self, nums: List[int]) -> bool:
        """
        BFS
        """
        q = Queue()
        q.put(0)
        while not q.empty():
            index = q.get()
            if index == len(nums) - 1:
                return True
            for i in range(1, nums[index] + 1):
                if index + i not in q.queue:
                    q.put(index + i)
        return False


s = Solution()
print(s.canJump([0]))

print(s.canJump([2,3,1,1,4]))
print(s.canJump([3,2,1,0,4]))
print(s.canJump([8,2,4,4,4,9,5,2,5,8,8,0,8,6,9,1,1,6,3,5,1,2,6,6,0,4,8,6,0,3,2,8,7,6,5,1,7,0,3,4,8,3,5,9,0,4,0,1,0,5,9,2,0,7,0,2,1,0,8,2,5,1,2,3,9,7,4,7,0,0,1,8,5,6,7,5,1,9,9,3,5,0,7,5]))