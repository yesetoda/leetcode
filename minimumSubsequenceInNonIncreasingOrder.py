class Solution:
    def minSubsequence( nums: list[int]) -> list[int]:
        if len(nums)==1:
            return nums
        nums.sort()
        sm = 0
        lsm = sum(nums)
        for i in range(len(nums)-1,-1,-1):
            if sm>lsm:
                "this is the upper if"
                return sorted(nums[i+1:],reverse = True)
            else:
                sm+=nums[i]
                lsm-=nums[i]
            if sm>lsm:
                print("this is the lower if")
                return sorted(nums[i:],reverse = True)
            print(sm,lsm)
            print(nums[i:])
        return []
    print(minSubsequence(nums = [99,99]))
# from random import choice
# x = [choice(['abcdefghijklmnopqrstuvwxyz']) for i in range(length)
# print(x)