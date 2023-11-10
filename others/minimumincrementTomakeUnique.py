class Solution:
    def minIncrementForUnique(nums: list[int]) -> int:
        nums.sort()
        leng = len(nums)
        cnt = 0
        for i in range(leng-1):
            if nums[i]==nums[i+1]:
                while nums[i+1] in nums:
                    nums[i+1]+=1
        return cnt
    print(minIncrementForUnique( nums = [3,2,1,2,1,7]))
                        
                