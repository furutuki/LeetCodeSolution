from typing import List


class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:

        def dfs(num: List[int], cur_res: List[int]):
            if not num:
                ret.append(cur_res)
                return
            else:
                for i in range(len(num)):
                    dfs(num[:i] + num[i + 1:], cur_res + [num[i]])

        ret = []
        dfs(nums, [])
        return ret
