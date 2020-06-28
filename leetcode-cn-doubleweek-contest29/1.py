from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        sum = 0
        min_num = 10000000
        max_num = 0
        for s in salary:
            if s < min_num:
                min_num = s
            if s > max_num:
                max_num = s
            sum += s
        return (sum - max_num - min_num) / (len(salary) - 2)


