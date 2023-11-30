from collections import Counter
class Solution:
    def numberOfWays( corridor: str) -> int:
        if Counter(corridor)["S"]%2==1:
            return 0
        p1 = 0
        p2 = 0
        out = 1
        inds = []
        cnt = 0
        while p1<len(corridor):
            while corridor[p1]!="S":
                p1+=1
                if p1== len(corridor):
                    break
            p2 = p1+1
            if p2<len(corridor):
                while corridor[p2]!="S":
                    p2+=1
                    if p2== len(corridor):
                        break
            if p1<len(corridor) and p2<len(corridor):
                if corridor[p1]==corridor[p2]=="S" :
                    if p1!=p2:
                        cnt+=2
                    else:
                        cnt+=2
                    inds.append([p1,p2])
            p1 = p2+1
        for i in range(len(inds)-1):
                # print(inds[i+1][0],inds[i][1],"this is the out:",out)
                out*=(inds[i+1][0]-inds[i][1])
        return out%(10**9+7)
from random import choice
x = [choice("SP") for i in range(10**5)]
corridor =  "".join(x)
print(corridor)
print(Solution.numberOfWays( corridor))