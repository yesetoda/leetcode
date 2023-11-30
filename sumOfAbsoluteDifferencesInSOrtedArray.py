class Solution:
    def getSumAbsoluteDifferences( nums: list[int]) -> list[int]:
        leng = len(nums)
        prefix = [0]*(leng+1)
        out = []
        for i in range(len(nums)):
            prefix[i+1] = nums[i]+prefix[i]
        for i in range(leng):
            out.append(nums[i]*(i)-prefix[i]+ prefix[leng]-prefix[i+1]-nums[i]*(leng-1-i))
        return out
    print(getSumAbsoluteDifferences(nums = [1,4,6,8,10]))
# from random import randint
# x = [randint(1,(i+1)*10)%1000 for i in range(10**5)]
# print(sorted(x))