passenger,plane = map(int,input().split())
seat = list(map(int,input().split()))
mx= 0
mn = 0
seat1 = seat.copy()
seat2 = seat.copy()
for i in range(passenger):
    seat1.sort()
    while seat1 and seat1[0]==0:
        seat1.pop(0)
    if not seat1:
        break
    mn += seat1[0]
    seat1[0]-=1

for i in range(passenger):
    seat2.sort()
    while seat2 and seat2[0]==0:
        seat2.pop(0)
    if not seat2:
        break
    mx += seat2[-1]
    seat2[-1]-=1

print(mx,mn)