from typing import List


class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        change = True
        while True:
            arr2 = arr.copy()
            flag = False
            for i in range(1, len(arr) - 1):
                if arr2[i] < arr2[i - 1] and arr2[i] < arr2[i + 1]:
                    arr[i] += 1
                    flag = True
                elif arr2[i] > arr2[i - 1] and arr2[i] > arr2[i + 1]:
                    arr[i] -= 1
                    flag = True
            if not flag:
                return arr


s = Solution()
print(s.transformArray([6,2,3,4]))
print(s.transformArray([1,6,3,4,3,5]))
