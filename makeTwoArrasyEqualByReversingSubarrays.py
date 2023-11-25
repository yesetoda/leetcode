# from collections import Counter
# class Solution:
#     def canBeEqual(target: list[int], arr: list[int]) -> bool:
#         a = Counter(target)
#         b = Counter(arr)
#         for ind,val in a.items():
#             if b[ind]<val:
#                 return False
#         return True
            
#     print(canBeEqual())
    
from random import randint
x = [randint(1,1000) for i in range(1000)]
print(x)