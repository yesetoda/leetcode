class Solution:
    def missingNumber( nums: list[int]) -> int:
        nums =  sorted(nums)
        last = nums[-1]
        for i in range(last):
            if i not in nums:
                return i
        return last+1
            
    nums = [2,0,1]
    print(missingNumber(nums))