class Solution:
    def intersection( nums1: list[int], nums2: list[int]) -> list[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        output = []
        for i in set1:
            if i in set2:
                output.append(i)
        return output
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    print(intersection(nums1,nums2))