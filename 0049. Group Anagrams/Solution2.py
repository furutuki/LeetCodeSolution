from typing import List

class Solution:

    def groupAnagrams(self, strs: List[str]):
        mapping = {}
        for item in strs:
            sorted_item = ''.join(sorted(item))
            mapping[sorted_item] = mapping.get(sorted_item, []) + [item]
        return mapping.values()

s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
