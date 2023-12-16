size,leng = map(int,input().split())
ls = list(map(int,input().split()))
ls.sort()
mn = 10000
for i in range(leng-size+1):
    mn = min(mn,ls[i+size-1]-ls[i])
print(mn)