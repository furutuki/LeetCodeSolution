class Solution:
    def climbStairs(self, n: int) -> int:
        prev_prev = 1
        prev = 2
        ret = 0
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            for i in range(n - 2):
                ret = prev_prev + prev
                prev_prev = prev
                prev = ret
        return ret
        # cnt = [1 for i in range(n)]
        # cnt[n - 2] = 2
        # for i in range(n - 3, -1, -1):
        #     cnt[i] = cnt[i + 1] + cnt[i + 2]
        # return cnt[0]


s = Solution()
print(s.climbStairs(1))
print(s.climbStairs(2))
print(s.climbStairs(3))
