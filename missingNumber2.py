class Solution:
    def findDisappearedNumbers(nums: list[int]) -> list[int]:
        # nums =  sorted(nums)
        # last = len(nums)
        # missing = []
        # for i in range(1,last+1):
        #     print(i)
        #     if i not in nums:
        #         missing.append(i)
        # return missing
        
        n = len(nums)
        num_set = set(nums)
        missing = []
        for i in range(1, n+1):
            if i not in num_set:
                missing.append(i)
        return missing
            
    nums = [1,1,1,1]
    print(findDisappearedNumbers(nums))