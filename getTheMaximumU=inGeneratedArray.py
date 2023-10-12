class Solution:
    def getMaximumGenerated( n: int) -> int:
        nums =[0,1]
        for i in range(2,n+1):
            if i%2==0:
                nums.append(nums[i//2])
            else:
                nums.append(nums[i//2]+nums[i//2+1])
        return max(nums) if n>0 else 0
    print(getMaximumGenerated(3))