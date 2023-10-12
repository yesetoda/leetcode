class Solution:
    def maxArrayValue(nums: list[int]) -> int:
        for i in range(len(nums)-1,0,-1):
            if nums[i]>=nums[i-1]:
                nums[i-1] += nums[i]
        return max(nums)
    print(maxArrayValue( nums = [5,7,3,3,0,2]))