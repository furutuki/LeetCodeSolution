from typing import List
import copy

class Solution:
    def dfs(self, ret: List[List[int]], cur_res: List[int], nums:List[int]):
        if len(nums) > 0:
            ret_copy = copy.deepcopy(ret)
            if len(ret_copy) > 0:
                for item in ret_copy:
                    item.append(nums[0])
                    ret.append(item)
            ret.append([nums[0]])
            self.dfs(ret, cur_res, nums[1:])


    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        self.dfs(ret, [], nums)
        ret.append([])
        return ret



s = Solution()
print(s.subsets([1,2,3]))