class Solution:
    def getSumAbsoluteDifferences(nums: list[int]) -> list[int]:
        prefix_sum = nums.copy()
        suffix_sum = nums.copy()
        print(nums)
        leng = len(nums)
        for i in range(1, len(nums)): 
            prefix_sum[i] = prefix_sum[i - 1] + prefix_sum[i]
            suffix_sum[-1-i]=suffix_sum[-1-i] + suffix_sum[-i] 
        print(prefix_sum,suffix_sum)
        out = []
        for i in range(leng):
            print(nums[i]*(i+1),prefix_sum[i-1] if i>0 else 0,suffix_sum[i+1] if i<leng-1 else 0 )
            out.append(nums[i]*i-(prefix_sum[i-1] if i>0 else 0 - suffix_sum[i+1] if i<leng else 0))
        print(out)
    print(getSumAbsoluteDifferences(nums = [2,3,5]))
