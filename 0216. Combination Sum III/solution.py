from typing import List


class Solution:

    def back_track(self, candidates: List[int], res: List[int], cur_res: List[int],  cur_sum: int, index: int, k:int, target: int):
        if cur_sum == target:
            if cur_res not in res and len(cur_res) == k:
                res.append(cur_res)
            return
        else:
            for i in range(index, len(candidates)):
                if cur_sum + candidates[i] > target or len(cur_res) > k:
                    break
                self.back_track(candidates, res, cur_res + [candidates[i]], cur_sum + candidates[i], i + 1, k, target)

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        candidates = [i + 1 for i in range(9)]
        res = []
        self.back_track(candidates, res, [], 0, 0, k, n)
        return res
