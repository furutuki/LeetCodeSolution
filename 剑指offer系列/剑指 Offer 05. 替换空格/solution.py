class Solution:
    def replaceSpace(self, s: str) -> str:
        res = ""
        if not s:
            return ""
        for ch in s:
            if ch == ' ':
                res += "%20"
            else:
                res += ch
        return res
