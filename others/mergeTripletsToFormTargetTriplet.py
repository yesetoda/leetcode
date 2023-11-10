class Solution:
    def mergeTriplets(triplets: list[list[int]], target: list[int]) -> bool:
        if target in triplets:
            return True
        
