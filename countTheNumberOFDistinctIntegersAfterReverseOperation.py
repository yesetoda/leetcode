class Solution:
    def countDistinctIntegers(nums: list[int]) -> int:
        out = set()
        for i in nums:
            out.add(i)
            out.add(int(str(i)[::-1]))
        return len(out)
    print(countDistinctIntegers(nums = [2,2,2]))
from random import randint
print([randint(1,10**6) for i in range(10**5)])