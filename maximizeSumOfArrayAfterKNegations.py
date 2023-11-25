class Solution:
    def largestSumAfterKNegations( nums: list[int], k: int) -> int:
        
        
        nums.sort()
        sm = 0
        for i in range(k):
            nums.sort()
            if nums[0]<0:
                nums[0]*=-1
            else:
                nums[0] *=-1
            mx = max(sm,sum(nums))
        return max(sm,sum(nums))
    print(largestSumAfterKNegations(nums = [1,3,2,6,7,9], k = 3))