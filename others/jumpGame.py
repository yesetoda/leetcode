class Solution:
    def canJump( nums: list[int]) -> bool:
        leng = len(nums)
        val = 1
        for i in range(len(nums)-2,-1,-1):
            print("val",val,"num",i,"==>",nums[i])
            if nums[i]>= val:
                val = 1
            else:
                val +=1
            
        if nums[0] < val:
                return False
        return True
    print(canJump( nums = [12804, 8, 94275, 66886, 12786, 13381, 47700, 68165, 9852, 87246] ))
# from random import randint
# print([randint(0, 10**5) for i in range(10)])