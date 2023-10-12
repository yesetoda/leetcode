class Solution:
    def minSubArrayLen(target: int, nums: list[int]) -> int:
        nums=list(set(nums))
        nums.sort(reverse= True)
        print(nums)
        cnt = 0
        for i in nums:
            if target-i>=0:
                target-=i
                cnt +=1
                print(i,target,cnt)
            else:
                cnt+=1
                return cnt
        return 0
    print(minSubArrayLen(target =213,nums =[12,28,83,4,25,26,25,2,25,25,25,12]))
        