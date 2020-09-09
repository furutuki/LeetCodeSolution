from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        ans = []
        # 单调双向队列，从左到右递减，存储数的下标
        q = deque()
        for i in range(len(nums)):
            # 移除队列右边所有不大于当前数的item
            while len(q) > 0 and nums[i] >= nums[q[-1]]:
                q.pop()
            # 队列右边添加当前数的索引
            q.append(i)
            # 如果队列左边的下标（对应滑动窗口的最大值）位于滑动窗口外，则移除它
            if i - k >= q[0]:
                q.popleft()
            # 添加当前的最大值到结果集中
            if i >= k - 1:
                ans.append(nums[q[0]])
        return ans
