from collections import Counter
class Solution:
    def intersect( nums1: list[int], nums2: list[int]) -> list[int]:
        freq1 = Counter(nums1)
        freq2 = Counter(nums2)
        out = []
        for i in freq2.keys():
            fr = 0
            if i in freq1.keys():
                fr = min(freq1[i],freq2[i])
            for j in range(fr):
                out.append(i)
        return out
    print(intersect(nums1 = [4,9,9,9,5], nums2 = [9,4,9,8,4]))