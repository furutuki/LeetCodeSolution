from typing import List


class Solution:

    def backtrace(self, nums: List[int], k: int,  step: int, res: List[int], ans: List[int]):
        if len(res) == k:
            ans.append(res[:])
            return

        for i in range(step, len(nums)):
            res.append(nums[i])
            self.backtrace(nums, k, i + 1, res, ans)
            res.pop()

    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        if n == 0 or k == 0:
            return ans

        nums = [i for i in range(n + 1)]
        self.backtrace(nums, k, 1, [], ans)
        return ans

s = Solution()
print(s.combine(4,2))