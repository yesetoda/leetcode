# class Solution:
#     def findPrefixScore(nums: list[int]) -> list[int]:
#         mx = 0
#         leng = len(nums)
#         x = [0]*leng
#         for i in range(leng):
#             mx = max(nums[i],mx)
#             x[i] = nums[i]+mx+(x[i-1] if i>0 else 0)
#         print(x)
#     print(findPrefixScore(nums = [1,1,2,4,8,16]))
from random import randint
x = [randint(1,100) for i in range(10**5)]
print(x)