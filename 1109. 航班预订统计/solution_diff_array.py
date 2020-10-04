from typing import List


class DiffArray:
    def __init__(self, arr: List[int]):
        self.diff = []
        self.diff.append(arr[0])
        for i in range(1, len(arr)):
            self.diff.append(arr[i] - arr[i - 1])

    def increment(self, i: int, j: int, val: int):
        self.diff[i] += val
        if j + 1 < len(self.diff):
            self.diff[j + 1] -= val

    def result(self) -> List[int]:
        ans = list()
        ans.append(self.diff[0])
        for i in range(1, len(self.diff)):
            ans.append(ans[i - 1] + self.diff[i])
        return ans


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        nums = [0 for _ in range(n)]
        diff_array = DiffArray(nums)
        for booking in bookings:
            i = booking[0] - 1
            j = booking[1] - 1
            val = booking[2]
            diff_array.increment(i, j, val)
        return diff_array.result()