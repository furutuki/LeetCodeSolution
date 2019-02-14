class Solution:
    def findMedianSortedArrays(self, nums1: 'List[int]', nums2: 'List[int]') -> 'float':
        new_list = list()
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                new_list.append(nums2[j])
                j += 1
            elif nums1[i] < nums2[j]:
                new_list.append(nums1[i])
                i += 1
            else:
                new_list.append(nums1[i])
                new_list.append(nums1[i])
                i += 1
                j += 1

        if i < len(nums1):
            new_list.extend(nums1[i:])
        if j < len(nums2):
            new_list.extend(nums2[j:])

        length = len(new_list)
        if length % 2 == 0:
            return (new_list[length // 2 - 1] + new_list[length // 2]) / 2
        else:
            return new_list[length // 2]


s = Solution()
print(s.findMedianSortedArrays([1,1,1,1,1,1,1,1,1,1,4,4],  [1,3,4,4,4,4,4,4,4,4,4]))
print(s.findMedianSortedArrays([1, 3],  [2]))
print(s.findMedianSortedArrays([1, 2],  [3, 4]))