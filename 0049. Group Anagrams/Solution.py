from typing import List


class ListNode:

    def __init__(self, val):
        self.origin_str = val
        self.sort_str = val

    def __lt__(self, other):
        return self.sort_str < other.sort_str


class Solution:

    def groupAnagrams(self, strs: List[str]):

        def convertNewList(node_list: List[ListNode]):
            for item in strs:
                node_list.append(ListNode(item))

        def sortNodeForList(node_list: List[ListNode]):
            for item in node_list:
                item.sort_str = "".join(sorted(list(item.origin_str)))

        def getResult(node_list: List[ListNode]):
            ret = []
            i = 0
            while i < len(node_list):
                sub_list = []
                while i < len(node_list):
                    sub_list.append(node_list[i].origin_str)
                    i += 1
                    if i >= len(node_list) or node_list[i].sort_str != node_list[i - 1].sort_str:
                        break
                ret.append(sub_list)
            return ret

        item_list = []
        convertNewList(item_list)
        sortNodeForList(item_list)
        item_list.sort()
        return getResult(item_list)


s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
