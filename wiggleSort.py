class Solution:
    def wiggleSort( nums: list[int]) -> None:
        for i in range(1, len(nums)):
            if (i % 2 == 1 and nums[i] < nums[i - 1]) or (i % 2 == 0 and nums[i] > nums[i - 1]):
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
        print(nums)
    wiggleSort( nums = [3,8,4,4,5,3,5,2,1,6,4])