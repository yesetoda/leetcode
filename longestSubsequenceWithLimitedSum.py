class Solution:
    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        end = 0
        start = 0
        while end<len(nums):
            if nums[start]>end