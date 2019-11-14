from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def sort_key(item: List[int]):
            return item[0]

        intervals.sort(key=sort_key)

        index = 0
        ret = []
        while index < len(intervals):
            start = intervals[index][0]
            stop = intervals[index][1]
            j = index + 1
            while j < len(intervals):
                if stop >= intervals[j][1]:
                    j += 1
                elif stop >= intervals[j][0]:
                    stop = intervals[j][1]
                    j += 1
                else:
                    break
            ret.append([start, stop])
            index = j
        return ret


s = Solution()
print(s.merge(
[[1,4],[2,3]]))
