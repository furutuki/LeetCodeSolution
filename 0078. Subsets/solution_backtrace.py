from typing import List


class Solution:
    def backtrace(self, nums: List[int], step: int, cur_res: List[int], res: List[List[int]]):
            if step == len(nums):
                res.append(list(cur_res))
                return
            cur_res.append(nums[step])
            self.backtrace(nums, step + 1, cur_res, res)
            cur_res.pop()
            self.backtrace(nums, step + 1, list(cur_res), res)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtrace(nums, 0, [], res)
        return res


s = Solution()
print(s.subsets([1,2,3]))