# class Solution:
#     def findPoisonedDuration(timeSeries: list[int], duration: int) -> int:
#         s =set()
#         for i in range(len(timeSeries)):
#             for j in range(timeSeries[i],timeSeries[i] + duration ):
#                 s.add(j)
#         return len(s)
#     print(findPoisonedDuration(timeSeries = [1,4], duration = 2))
from random import randint
x = sorted([randint(0,10**4) for i in range(10**3)])
print(x)