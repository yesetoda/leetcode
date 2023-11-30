x ,y,z = 0,0,0
for i in range(int(input())):
    a,b,c = map(int,input().split())
    x+=a
    y+=b
    z+=c
print("YES" if x==0 and y==0 and z==0 else "NO")
    