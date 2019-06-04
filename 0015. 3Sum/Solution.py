class Solution:

    def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':
        nums.sort()
        result = list()

        for x in range(len(nums) - 2):

            if x > 0 and nums[x] == nums[x - 1]:
                continue

            target = nums[x]
            low = x + 1
            high = len(nums) - 1

            while low < high:

                if nums[low] + nums[high] + target > 0:
                    high -= 1

                elif nums[low] + nums[high] + target < 0:
                    low += 1

                else:
                    result.append([target, nums[low], nums[high]])

                    while low + 1 < high and nums[low] == nums[low + 1]:
                        low += 1
                    while high - 1 > low and nums[high] == nums[high - 1]:
                        high -= 1

                    low += 1
                    high -= 1

        return result


s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1]))
print(s.threeSum([0, 0, 0, 0]))
