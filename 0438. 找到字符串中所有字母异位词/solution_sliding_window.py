from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # 目标字符集和窗口字符集
        need, window = dict(), dict()

        ans = []

        # 统计目标字符集
        for ch in p:
            if ch in need:
                need[ch] += 1
            else:
                need[ch] = 1

        # 窗口的左右边界，左开右闭
        left, right = 0, 0

        # 覆盖的字符个数
        valid = 0

        while right < len(s):
            # 移入一个字符到窗口中
            ch = s[right]
            right += 1

            if ch in need and need[ch] > 0:
                if ch in window:
                    window[ch] += 1
                else:
                    window[ch] = 1
                if window[ch] == need[ch]:
                    valid += 1

            while right - left >= len(p):
                # 判断是否找到了合法的子串
                if valid == len(need):
                    ans.append(left)

                # 移出一个字符
                d = s[left]
                left += 1

                if d in need and need[d] > 0:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
                    if window[d] == 0:
                        del window[d]

        return ans