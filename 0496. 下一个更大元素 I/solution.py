from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        "单调递减栈"
        stack = list()

        "存放nums2中每个元素的下一个更大的数"
        next_grater_num = [0 for i in range(len(nums2))]

        "存放nums2中每个元素对应的下标"
        num_to_index = dict()

        "计算nums2中每个元素对应的下一个更大的数，存放到next_grater_num数组中"
        for i in range(len(nums2) - 1, -1, -1):
            num_to_index[nums2[i]] = i
            while len(stack) and stack[-1] <= nums2[i]:
                stack.pop()
            next_grater_num[i] = -1 if not len(stack) else stack[-1]
            stack.append(nums2[i])

        "遍历nums1中的每个元素，根据dict找到nums2中对应的下标，然后查找数组next_grater_num即可得到答案"
        ans = []
        for item in nums1:
            ans.append(next_grater_num[num_to_index[item]])
        return ans
