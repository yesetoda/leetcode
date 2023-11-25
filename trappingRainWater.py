# class Solution:
#     def trap( height: list[int]) -> int:
#         next_mx = [max(height[i+1:]) for i in range(len(height)-1)]
#         # print(next_mx)
#         start = 0
#         end = 1
#         leng = len(height)
#         total = 0
#         while start<leng:
#             block_area = 0
#             while end<leng:
#                 # print(height[start]>height[end])
#                 if height[start]>height[end] and end<leng-1:
#                     block_area+=height[end]
#                     end+=1
#                     # print("this is the block area",block_area)
#                 else:
#                     # print(start,end,height[start],height[end])
#                     total+=min(height[start],next_mx[start])*(end-start-1)
#                     # print(total)
#                     total-=block_area
#                     # print("this is the total:",total)
#                     block_area = 0
#                     start=end
#                     end+=1
#             start+=1
#             end = start
#         # if end==leng and height[end-1]<height[temp]:
#         #         print("this is te condition")
#         return total
#     print(trap(height = [0,1,0,2,1,0,1,3,2,1,2,1]))
    
    
from random import randint
x = [randint(0,100) for i in range(2*10**4)]
print(x)