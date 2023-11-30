n,k,q =  map(int,input().split())
x = [0]*200001
for i in range(n):
    t1,t2 = map(int,input().split())
    for i in range(t1,t2+1):
        x[i] += 1

for j in range(q):
    admis = 0
    q1,q2 = map(int,input().split())
    for i in range(q1,q2+1):
        if x[i] >=k:
            admis+=1
    print(admis)