class Solution:
    def numSubarrayProductLessThanK( nums: list[int], k: int) -> int:
        cnt = 0
        for i in range(len(nums)):
            cnm = 1
            for j in range(i,len(nums)):
                cnm*=nums[j]
                if cnm>=k:
                    break
                else:
                    cnt+=1
                # print(i,j,cnt,cnm)
        return cnt
    
#     # print(numSubarrayProductLessThanK(nums = [1,2,3], k = 0))
from random import randint
x = [randint(1,1000) for i in range(3*10**4)]
print(x)