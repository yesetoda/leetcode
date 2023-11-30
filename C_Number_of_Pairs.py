lns = int(input())
for i in range(lns):
    n,l,r = map(int,input().split())
    ls = list(map(int,input().split()))
    cnt = 0
    for i in range(n-1):
        for j in range(i+1,n):
            if l<=ls[i]+ls[j]<=r:
                cnt+=1
    print(cnt)
import sys,io,os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
read = lambda: map(int,input().split())
O = []
for _ in range(lns):
    a = sorted(ls)
    pl, pr = n-1, n-1
    v = 0
    for p in range(n):
        while pl>=p and a[pl]+a[p]>=l: pl-=1
        while pr>=p and a[pr]+a[p]>r: pr-=1
        v += max(p,pr)-max(p,pl)
    O.append(str(v))
print('\n'.join(O))
# from random import randint
# x = " ".join([str(randint(1,100)) for i in range(500)])
# print(x)
