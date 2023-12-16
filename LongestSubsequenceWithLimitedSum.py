# class Solution:
#     def answerQueries(nums: list[int], queries: list[int]) -> list[int]:
#         nums.sort()
#         out = []
#         prefix = [nums[0]]
#         for i in range(1,len(nums)):
#             prefix.append(prefix[i-1]+nums[i])
#         for limit  in queries:
#             found = False
#             for i in range(len(nums)-1,-1,-1):
#                 if prefix[i]<=limit:
#                     out.append(i+1)
#                     found = True
#                     break
#             if not found:
#                 out.append(0)
#         return out
#     print(answerQueries(nums = [2,3,4,5] ,queries = [1,2]))
from random import randint
x = [randint(1,100) for i in range(1000)]
print(x)