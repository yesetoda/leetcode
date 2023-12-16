# class Solution:
#     def maxSubArray(nums: list[int]) -> int:
#         st = 0
#         en = len(nums)-1
#         sm = sum(nums)
#         temp = sm
#         while st!=en:
#             if nums[st]<nums[en]:
#                 temp-=nums[st]
#                 st+=1
                
#             elif nums[st]>nums[en]:
#                 temp-=nums[en]
#                 en-=1
#             else:
#                 if st+1<en-1:
#                     if nums[st+1]<nums[en-1]:
#                         temp-=nums[st]
#                         st+=1
#                     elif nums[st+1]>nums[en-1]:
#                         temp-=nums[en]
#                         en-=1
#             sm= max(sm,temp)
#             print(sm,sorted(nums[st:en+1]))
#         return sm
#     print(maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4]))
from random import randint
x = [randint(-100,100) for i in range(10**5)]
print(x)