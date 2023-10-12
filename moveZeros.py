# class Solution:
#     def moveZeroes( nums: list[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         count = 0
#         output = []
#         for i in nums:
#             if i == 0:
#                 count+=1
#             else:
#                 output.append(i)
                
#         for j in range(count):
#             output.append(0)
            
#         output
#     nums = [0,1,0,3,12]
#     print(moveZeroes(nums))

class Solution:
    def moveZeroes(nums: list[int]) -> None:
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[next_non_zero] = nums[i]
                next_non_zero += 1
        while next_non_zero < len(nums):
            nums[next_non_zero] = 0
            next_non_zero += 1
        return nums
    nums = [0,1,0,3,12]
    print(moveZeroes(nums))