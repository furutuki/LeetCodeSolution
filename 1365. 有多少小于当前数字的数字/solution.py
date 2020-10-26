from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        cnt = [0 for _ in range(101)]
        s = [0 for _ in range(101)]

        for item in nums:
            cnt[item] += 1

        for i in range(1, len(cnt)):
            s[i] = s[i - 1] + cnt[i - 1]

        ans = []
        for item in nums:
            ans.append(s[item])
        return ans


s = Solution()
print(s.smallerNumbersThanCurrent([8,1,2,2,3]))