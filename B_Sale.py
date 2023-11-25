amount,carry  = map(int,input().split())
x = list(map(int,input().split()))
x.sort()
srt = []
sm = 0
cnt  = 0
for i in x:
    if cnt>=carry:
        break
    if  i<0:
        sm+=-1*i
        cnt+=1
    else:
        break
print(sm)