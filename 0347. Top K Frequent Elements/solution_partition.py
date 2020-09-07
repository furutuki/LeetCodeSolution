from typing import List


class Node:
    def __init__(self, val:int):
        self.val = val
        self.cnt = 1

class Solution:

    def partition(self, nums: List[Node], low: int, high: int):
        i, j = low + 1, high
        cnt = nums[low].cnt
        while True:
            while nums[i].cnt < cnt and i < high:
                i += 1
            while nums[j].cnt > cnt:
                j -= 1
            if i >= j:
                break
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        nums[low], nums[j] = nums[j], nums[low]
        return j

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        node_map = dict()
        val_set = set()
        l = list()
        for item in nums:
            if item in val_set:
                node_map[item].cnt += 1
            else:
                val_set.add(item)
                node = Node(item)
                node_map[item] = node
                l.append(node)

        ans = []
        k = len(l) - k
        low, high = 0, len(l) - 1
        while low < high:
            p = self.partition(l, low, high)
            if p == k:
                for item in l[k:]:
                    ans.append(item.val)
                return ans
            elif p > k:
                high = p - 1
            else:
                low = p + 1
        for item in l[low:]:
            ans.append(item.val)
        return ans


s = Solution()
print(s.topKFrequent([1,1,1,2,2,3], 2))
print(s.topKFrequent([1], 1))