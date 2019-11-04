from typing import List


class Solution:

    def back_track(self, candidates: List[int], res: List[int], cur_res: List[int],  cur_sum: int, index: int, target: int):
        if cur_sum == target:
            if cur_res not in res:
                res.append(cur_res)
            return
        else:
            for i in range(index, len(candidates)):
                if cur_sum + candidates[i] > target:
                    break
                self.back_track(candidates, res, cur_res + [candidates[i]], cur_sum + candidates[i], i + 1, target)

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        self.back_track(candidates, res, [], 0, 0, target)
        return res


s = Solution()
print(s.combinationSum2([10,1,2,7,6,1,5], 8))
