from collections import Counter
class Solution:
    def findLonely( nums: list[int]) -> list[int]:
        out = set()
        cnt = Counter(nums)
        print(cnt)
        for num, count in cnt.items():
            if count==1 and num+1 not in cnt and num-1 not in cnt:
                out.add(num)
        return list(out)
    print(findLonely(nums = [1,2,3,4,5,6,1,2,3]))
# from random import randint
# print([randint(1,1000000) for i in range(100000)])