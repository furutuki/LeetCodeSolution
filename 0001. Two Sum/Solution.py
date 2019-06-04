class Solution:

    def twoSum(self, nums: 'List[int]', target: int) -> 'List[int]':

        def get_sort_key(nums_list):
            return nums_list[0]

        new_list = []
        for x in range(0, len(nums)):
            new_item = [nums[x], x]
            new_list.append(new_item)

        new_list.sort(key=get_sort_key)

        start = 0
        end = len(new_list) - 1
        res = []
        while start < end :
            if new_list[start][0] + new_list[end][0] > target:
                end -= 1
            elif new_list[start][0] + new_list[end][0] < target:
                start += 1
            else:
                res.append(new_list[start][1])
                res.append(new_list[end][1])
                return res



s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
print(s.twoSum([3, 2, 4], 6))
