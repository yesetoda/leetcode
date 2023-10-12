class Solution:
    def dominantIndex(nums: list[int]) -> int:
        unsortednums = nums
        sortednums = sorted(nums,reverse=True)
        for i in sortednums[1:]:
            if sortednums[0]<2*i:
                return -1
        return unsortednums.index(sortednums[0])
    nums = [1,2,3,4]
    print(dominantIndex(nums))