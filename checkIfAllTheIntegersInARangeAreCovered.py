# class Solution:
#     def isCovered(ranges: list[list[int]], left: int, right: int) -> bool:
#         out = [0]*51
#         for i in ranges:
#             out[i[0]] += 1
#             out[i[1]+1] -= 1
#         prefix = [out[0]]
        
#         for i in range(1,51):
#             prefix.append(prefix[i-1]+out[i])
#         for i in range(left,right+1):
#             if prefix[i] ==0:
#                 return False
#         return True
#     print(isCovered( ranges = [[1,10],[10,20]], left = 21, right = 21 ))
from random import randint
x = [[randint(1,21),randint(21,50)] for i in range(50)]
print(x)