# class Solution:
#     def numberOfPoints( nums: list[list[int]]) -> int:
#         cars = set()
#         for col in range(len(nums)):
#             for j in range(nums[col][0],nums[col][1]+1):
#                 cars.add(j)
#             # print(cars)
#         return len(cars)
#     print(numberOfPoints(nums = [[1,3],[5,8]]))
from random import randint
x = [[x:=randint(1,100),randint(x,100)] for  j in range(100)]
print(x)