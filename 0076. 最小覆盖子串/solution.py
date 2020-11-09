from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 目标字符集和窗口字符集
        need, window = dict(), dict()

        # 统计目标字符集
        for ch in t:
            if ch in need:
                need[ch] += 1
            else:
                need[ch] = 1

        BIG_NUMBER = 1000000
        
        # 最小窗口的歧视坐标和长度
        start, length = 0, BIG_NUMBER

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

            while valid == len(need):
                # 更新最小窗口
                if right - left < length:
                    length = right - left
                    start = left

                # 移出一个字符
                d = s[left]
                left += 1

                if d in need and need[d] > 0:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
                    if window[d] == 0:
                        del window[d]

        return "" if length == BIG_NUMBER else s[start: start + length]

s = Solution()
print(s.minWindow("ADOBECODEBANC", "ABC"))