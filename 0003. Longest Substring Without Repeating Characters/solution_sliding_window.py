class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = dict()

        ans = 0

        # 窗口的左右边界，左开右闭
        left, right = 0, 0

        while right < len(s):
            # 移入一个字符到窗口中
            ch = s[right]
            right += 1

            if ch in window:
                window[ch] += 1
            else:
                window[ch] = 1

            while window[ch] > 1:
                # 移出一个字符
                d = s[left]
                left += 1

                window[d] -= 1
                if window[d] == 0:
                    del window[d]

            ans = max(ans, right - left)

        return ans