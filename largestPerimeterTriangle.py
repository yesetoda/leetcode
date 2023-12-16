class Solution:
    def largestPerimeter(nums: list[int]) -> int:
        leng = len(nums)
        nums.sort()
        out = 0
        print(nums)
        
        for i in range(leng-2):
            if sum(nums[i:i+2])>nums[-1]:
                out = max(out,nums[i]+nums[i+1]+nums[-1])       
        return out
    print(largestPerimeter([3,6,2,3]))