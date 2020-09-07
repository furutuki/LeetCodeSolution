from typing import List
import heapq


class Node:
    def __init__(self, val:int):
        self.val = val
        self.cnt = 1

    def __lt__(self, other):
        return self.cnt < other.cnt

    def __eq__(self, other):
        return self.cnt == other.cnt

class Solution:


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
        heap_arr = []
        for node in l:
            if len(heap_arr) < k:
                heapq.heappush(heap_arr, node)
            elif heap_arr[0].cnt < node.cnt:
                heapq.heappop(heap_arr)
                heapq.heappush(heap_arr, node)
        while heap_arr:
            ans.append(heapq.heappop(heap_arr).val)
        return ans


s = Solution()
print(s.topKFrequent([1,1,1,2,2,3], 2))
print(s.topKFrequent([1], 1))