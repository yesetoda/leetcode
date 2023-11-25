# class Solution:
#     def maxSum(grid: list[list[int]]) -> int:
#         rows = len(grid[0])
#         columns = len(grid)
#         mx = 0
#         for col in range(columns-2):
#             for  row in range(rows-2):
#                 urs = sum(grid[col][row:row+3])
#                 cs = grid[col+1][row+1]
#                 lrs = sum(grid[col+2][row:row+3])
#                 # print(urs,cs,lrs)
#                 mx = max(mx,urs+cs+lrs)
#         return mx
#     print(maxSum(grid = [[1,2,3],[4,5,6],[7,8,9]]))
from random import randint
x = [[randint(0,10) for i in range(10)] for i in range(150)]
print(x)