# class Solution:
#     def predictTheWinner(nums: list[int]) -> bool:
#         p1,p2 = 0,0
#         while nums:
#             if nums[0]>nums[-1]:
#                 p1+=nums.pop(0)
#             else:
#                 p1+=nums.pop(len(nums)-1)
#             if nums:
#                 if nums[0]>nums[-1]:
#                     p2+=nums.pop(0)
#                 else:
#                     p2+=nums.pop(len(nums)-1)
#         return p1>=p2,(p1,p2)=
#     print(predictTheWinner( nums = [1,5,233,7]))
        
class Solution:
    def predictTheWinner( nums: list[int]) -> bool:
        leng = len(nums)
        for i in range(leng//2):
            if nums[0]+nums[1]>nums[]