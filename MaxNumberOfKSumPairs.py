class Solution:
    def maxOperations( nums: list[int], k: int) -> int:
        nums.sort()
        st = 0
        en = len(nums)-1
        op = 0
        while st < en:
            if nums[st]+nums[en]==k:
                st+=1
                en-=1 
                op+=1
            elif  nums[st]+nums[en]<k:
                st+=1
            else:
                en-=1
        return op
    print(maxOperations (nums = [3,1,3,4,3], k = 6))