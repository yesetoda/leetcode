class Solution:
    def findMaxConsecutiveOnes( nums: list[int]) -> int:
        ones = []
        cons = 0
        for i in nums:
            if i ==1:
                cons+=1
            else:
                ones.append(cons)
                cons=0
        ones.append(cons)
        return max(ones)
    nums =[1,1,0,1,1,1]
    print(findMaxConsecutiveOnes(nums))