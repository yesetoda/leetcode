class Solution:
    def twoSum(nums: list[int], target: int) -> list[int]:
        n = nums[::]
        n.sort()
        print(n)
        x= 0
        start =n[x]
        eind = len(n)-1
        end = n[eind]
        while True:
            if start+end == target:
                out1 = nums.index(start)
                nums[out1] = "x"
                out2 = nums.index(end)
                return [out1,out2]
            elif start+end > target:
                eind-=1
                end = n[eind]
            elif start+end < target:
                x+=1
                start = n[x]
    nums = [3,3]
    target = 6
    print(twoSum(nums,target))