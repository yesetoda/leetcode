houses = [1,2,3,4,5,6,7,8,9,0]
vals =[]
for i in range(len(houses)):
    nw = [houses[i]]
    for j in range(i+2,len(houses)):
        nw.append(houses[i]+houses[j])
    vals.append(nw)
print(vals)