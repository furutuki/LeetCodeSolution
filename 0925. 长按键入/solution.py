class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        m = len(name)
        n = len(typed)
        i, j = 0, 0
        while i < m and j < n:
            ch = name[i]
            s1 = 1
            while i + 1 < m and name[i] == name[i + 1]:
                i += 1
                s1 += 1
            if typed[j] != ch:
                return False
            s2 = 1
            while j + 1 < n and typed[j] == typed[j + 1]:
                j += 1
                s2 += 1
            if s1 > s2:
                return False
            i += 1
            j += 1
        return i == m and j == n


s = Solution()
print(s.isLongPressedName("alex", "aaleex"))
print(s.isLongPressedName("saeed", "ssaaedd"))
print(s.isLongPressedName("leelee", "lleeelee"))
print(s.isLongPressedName("laiden", "laiden"))
print(s.isLongPressedName("pyplrz","ppyypllr"))