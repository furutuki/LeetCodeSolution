class Solution:
    def longestCommonPrefix(self, strs: 'List[str]') -> 'str':
        if len(strs) == 0:
            return ""

        cmn_str = strs[0]
        for i in range(1, len(strs)):
            j = 0
            while j < len(cmn_str) and j < len(strs[i]):
                if cmn_str[j] == strs[i][j]:
                    j += 1
                else:
                    break
            if j > 0:
                cmn_str = strs[i][:j]
            else:
                cmn_str = ""
        return cmn_str


s = Solution()
print(s.longestCommonPrefix(["flower", "flow", "flight"]))
print(s.longestCommonPrefix(["dog", "racecar", "car"]))
