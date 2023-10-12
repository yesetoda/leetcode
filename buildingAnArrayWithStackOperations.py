class Solution:
    def buildArray( target: list[int], n: int) -> list[str]:
        nums = [i for i in range(1,n+1)]
        out2 = []
        out = []
        for i in nums:
            if i in target:
                out.append("Push")
                out2.append(i)
            else:
                out.append("Push")
                out.append("Pop")
            if out2==target:
                break
        return out
    print(buildArray(target = [1,2,3], n = 3))
from random import randint
x = [1]
for i in range(1,100):
    val = randint(max(x),i*2)
    x.append(val) if val not in x and val<100 else print(x)
print([x])