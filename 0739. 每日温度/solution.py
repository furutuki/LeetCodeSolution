from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        "单调递减栈"
        stack = []

        "单调递减栈元素对应的下标"
        idx_stack = []

        "下一个更大的数"
        # arr = [0 for _ in range(len(T))]

        "下一个更大的数与当前的下标的差值"
        idx = [0 for _ in range(len(T))]

        for i in range(len(T) - 1, -1, -1):
            while len(stack) and stack[-1] <= T[i]:
                stack.pop()
                idx_stack.pop()
            # arr[i] = stack[-1] if len(stack) else -1
            idx[i] = idx_stack[-1] - i if len(idx_stack) else 0
            idx_stack.append(i)
            stack.append(T[i])
        return idx


s = Solution()
print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))