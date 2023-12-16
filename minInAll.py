a = [[1,2,3,1,2],[4,1,5,3,4],[5,8,3,2,1],[7,4,8,3,2,]]
x = set(a[0])
for i in range(1,len(a)):
    x = x.intersection(a[i])
print(min(x))