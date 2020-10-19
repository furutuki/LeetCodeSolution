from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        "单调递减栈"
        stack = list()

        n = len(nums)
        ans = [0 for _ in range(n)]
        for i in range(2 * n - 1, -1, -1):
            while len(stack) and stack[-1] <= nums[i % n]:
                stack.pop()
            ans[i % n] = stack[-1] if len(stack) else -1
            stack.append(nums[i % n])
        return ans
