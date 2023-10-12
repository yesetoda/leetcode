class Solution:
    def minOperations(nums: list[int], k: int) -> int:
        mx = 0
        nums = nums[::-1]
        for i in range(1,k+1):
            ind = nums.index(i)
            if ind>mx:
                mx = ind
        return mx+1
    print(minOperations(nums = [3,2,5,3,1], k = 3))
from random import randint
print([randint(1,50) for i in range(50)])