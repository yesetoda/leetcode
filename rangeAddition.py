leng = 5
ar = [0]*(100)
x =  [[2,4,6],[5,6,8],[1,9,-4]]
for i in x:
    s,e,u = i[0],i[1],i[2]
    ar[s]+=u
    ar[e+1]-=u
for i in range(1,leng):
    ar[i] = ar[i]+ar[i-1]
print(ar)