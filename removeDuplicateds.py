class Solution:
    def removeDuplicates(nums: list[int]) -> int:
        lastind = 0
        for i in set(nums):
            cnt = nums.count(i)
            if cnt>2:
                for j in range(cnt-2):
                    nums.remove(i)
                    nums.append(i)
                lastind+=2
            else:
                lastind+=cnt
        return lastind,nums,nums[:lastind]
    print(removeDuplicates(nums = [0,0,1,1,1,1,2,3,3]))