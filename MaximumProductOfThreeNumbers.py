class Solution:
    def maximumProduct( nums: list[int]) -> int:
        leng = len(nums)
        mx = -10000**3
        for i in range(leng-2):
            for x in range(i+1,leng):
                for j in range(i+2,leng):
                    mx = max(nums[i]*nums[x]*nums[j],mx)
                    print(mx,nums[i],nums[x],nums[j])
        return mx
    print(maximumProduct([9,1,5,6,7,2]))