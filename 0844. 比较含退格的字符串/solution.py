class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        ss = list()
        tt = list()
        for ch in S:
            if ch == '#' and len(ss):
                ss.pop()
            elif ch != '#':
                ss.append(ch)
        for ch in T:
            if ch == '#' and len(tt):
                tt.pop()
            elif ch != '#':
                tt.append(ch)
        return ss == tt
