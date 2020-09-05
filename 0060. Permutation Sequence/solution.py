class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [0 for _ in range(n)]
        factor = 1
        for i in range(n):
            nums[i] = i + 1
            factor *= i + 1
        ans = ""
        while len(nums) > 0:
            factor //= len(nums)
            digit_index = (k - 1) // factor
            ans += str(nums[digit_index])
            k %= factor
            del nums[digit_index]
        return ans

s = Solution()
print(s.getPermutation(4,10))