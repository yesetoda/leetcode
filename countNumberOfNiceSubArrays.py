# class Solution:
#     def numberOfSubarrays(nums: list[int], k: int) -> int:
#         nums.append(0)
#         even = 0
#         for i in range(min(k,len(nums))):
#             if nums[i]%2==0:
#                 even+=1
#         odd = k-even
#         freq = {"even":even,"odd":odd}
#         cnt = 1 if freq["odd"]==k else 0
#         for i in range(len(nums)-k):
#             for j in range(i+k,len(nums)):
#                 if nums[j]%2==1:
#                     freq["odd"]+=1
#                 else:
#                     freq["even"]+=1
#                 if freq["odd"]>k:
#                     if nums[i]%2==1:
#                         freq["odd"]-=1
#                     else:
#                         freq["even"]-=1
#                     break
#                 print(i,j,freq,freq["odd"],freq["odd"]==k)
#                 cnt +=1 if freq["odd"]==k else 0
#         print(cnt)
#     numberOfSubarrays( nums = [2,2,2,1,2,2,1,2,2,2], k = 2)

import functools
from itertools import accumulate


class Solution:
    def numberOfSubarrays( nums: list[int], k: int) -> int:
        ls = [0 if i%2==0 else 1 for i in nums]
        print(ls)
        ls = list(accumulate(ls))
        print(ls)
        bk = len(nums)-1
        fr = 0
        cnt = 0
        while bk-fr>=k:
            if ls[bk]>k:
                bk-=1
            if ls[bk]==ls[fr]==k:
                fr+=1
                cnt+=1
    numberOfSubarrays(nums = [2,2,2,1,2,2,1,2,2,2], k = 2)