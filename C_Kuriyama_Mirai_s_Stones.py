leng = int(input())
cost = list(map(int,input().split()))
prefix = [0]
for i in range(leng):
    prefix.append(prefix[i]+cost[i])
cs = sorted(cost)
ps = [0]
for i in range(leng):
    ps.append(ps[i]+cs[i])
for j in range(int(input())):
    type,l,r = map(int,input().split())
    if type==1:
        print(prefix[r]-(prefix[l-1]))
    else:
        print(ps[r]-(ps[l-1]))
