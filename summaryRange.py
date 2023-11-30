class Solution:
    def summaryRanges(nums: list[int]) -> list[str]:
        nums.append(2**31+1)
        prev = 0
        cur = 0
        out = []
        while cur+1<len(nums):
            while cur+1<len(nums) and nums[cur+1]-nums[cur]<= 1:
                cur+=1
            else:
                out.append([prev,cur])
                print(prev,cur)
                prev = cur+1
                cur+=1
        out2 = []
        for i in out:
            if i[0]==i[1]:
                out2.append(f"{nums[i[0]]}")
            else:
                out2.append(f"{nums[i[0]]}-->{nums[i[1]]}")
        return out2
    print(summaryRanges(nums = [-2147483648,-2147483647,2147483647]))