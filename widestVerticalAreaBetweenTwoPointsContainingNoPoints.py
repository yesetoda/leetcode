# class Solution:
#     def maxWidthOfVerticalArea(points: list[list[int]]) -> int:
#         points.sort()
#         mx = 0
#         for i in range(len(points)-1):
#             mx = max(mx,points[i+1][0]-points[i][0])
#         return mx
#     print(maxWidthOfVerticalArea(points = [[8,7],[9,9],[7,4],[9,7]]))
from random import randint
x = [[randint(0,100),randint(0,100)] for i in range(10**4)]
print(x)