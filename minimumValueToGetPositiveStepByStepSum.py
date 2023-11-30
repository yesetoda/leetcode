# class Solution:
#     def minStartValue( nums: list[int]) -> int:
#         leng = len(nums)
#         mn = nums[0]
#         prefix = [nums[0]]
#         for i in range(1,leng):
#             prefix.append(prefix[i-1]+nums[i])
#             mn = min(prefix[i],nums[i],mn)
#         return -mn+1 if mn<0 else mn
#     print(minStartValue(nums = [1,-2,-3]))
        
from random import randint
x = [randint(-100,100) for i in range(100)]
print(x)

